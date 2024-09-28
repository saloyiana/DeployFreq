from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient, ASCENDING
import datetime
import urllib.parse
import os 

app = FastAPI()

# Define the path to the secrets
secrets_path = '/etc/db-secrets/'

# Getting the required values
def get_secret(file_name):
    with open(os.path.join(secrets_path, file_name), 'r') as file:
        return file.read().strip()

# Fetch MongoDB connection settings from files
username = urllib.parse.quote_plus(get_secret('username'))
password = urllib.parse.quote_plus(get_secret('password'))
host = get_secret('host')
port = get_secret('port')
database_name = get_secret('database_name')

# Build MongoDB URI
mongo_uri = f'mongodb://{username}:{password}@{host}:{port}/{database_name}'

# Connect to MongoDB
mongo_client = MongoClient(mongo_uri)
db = mongo_client[database_name]
collection = db['deployment_frequencies']

# Ensure the index on the product field is created at startup
collection.create_index([("product", ASCENDING)], unique=True)

class DeploymentUpdate(BaseModel):
    deployment_name: str
    product: str

@app.post("/update_frequency")
async def update_frequency(update: DeploymentUpdate):
    current_time = datetime.datetime.utcnow()
    product = update.product
    deployment_name = update.deployment_name

    # Ensure the product index is created if not already
    collection.create_index([("product", ASCENDING)], unique=True)

    # Increment the deployment's frequency
    result = collection.find_one_and_update(
        {'product': product},
        {
            '$inc': {f'deployments.{deployment_name}.frequency': 1, 'total_frequency': 1},
            '$set': {f'deployments.{deployment_name}.last_updated': current_time},
        },
        upsert=True,
        return_document=True
    )
    if result:
        return {"message": "Frequency updated", "deployment": deployment_name}
    else:
        raise HTTPException(status_code=500, detail="Failed to update frequency")

@app.get("/get_frequencies/{product}")
async def get_frequencies(product: str):
    result = collection.find_one({'product': product})
    if result:
        # Remove the '_id' field from the result to avoid issues with ObjectId
        result.pop('_id', None)
        return result
    else:
        raise HTTPException(status_code=404, detail="product not found")

@app.get("/get_all_products")
async def get_all_products():
    result = collection.distinct("product")
    return {"products": result}

# Run the FastAPI app
# uvicorn main:app --reload --host 0.0.0.0 --port 8000