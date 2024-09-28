DORA stands for the **DevOps Research and Assessment** group. It's a research program focused on understanding and improving DevOps practices. DORA is known for its work on identifying key metrics and practices that lead to high performance in software delivery and operations.

**DORA Key Metrics:** DORA identifies four key metrics that are critical for measuring software delivery performance:
   - **Deployment Frequency**: How often code is deployed to production.
   - **Lead Time for Changes**: The time it takes from committing code to deploying it to production.
   - **Change Failure Rate**: The percentage of changes that fail after deployment.
   - **Time to Restore Service**: The time it takes to recover from a failure in production.

These metrics help organizations measure and improve their DevOps performance, driving faster, more reliable software delivery.

# DeployFreq 

The **DeployFreq** is an application designed to automate one of the key metrics of DORA which is the *deployment frequency*. It efficiently manages and monitors deployment frequencies across various products, providing insights into deployment activities.

### Features
- **Update Deployment Frequency**: Increment service deployment counts for a specific product.
- **Get Frequencies by Product**: Retrieve service deployment statistics for a specific product.
- **Get All Products**: List all tracked products and their service deployments.

## Installation

**Note:** The provided deployment configuration is designed to run on Kubernetes for now; however, there is also an option to build and run it as a service on a VM.

### Steps: 
Run 
```   
make up
```   
and it will bring up the app for you!

### DeployFreq Endpoints
- `POST /update_frequency`: Update the frequency of a service deployment for a given product.   
- `GET /get_frequencies/{product}`: Retrieve the deployment frequencies for a specific product services.   
- `GET /get_all_products`: Get a list of all products.

## CI/CD Integration

To integrate the DeployFreq into your CI/CD pipeline, you can choose between a Bash script or a Python script. Both options will configure a job to install dependencies and run the script as part of the deployment process.   

You can include the respective scripts in various CI/CD tools as follows:
- **GitHub Actions:**  
  - path: `cicd-examples/bash-based/github-actions.yml`  
  - path: `cicd-examples/python-based/github-actions.yml`    
- **GitLab CI:**
  - path: `cicd-examples/bash-based/.gitlab-ci.yml`    
  - path: `cicd-examples/python-based/g.gitlab-ci.yml`     
- **Jenkins:**
  - path: `cicd-examples/bash-based/Jenkinsfile`    
  - path: `cicd-examples/python-based/Jenkinsfile`   
- **Azure Pipelines:**
  - path: `cicd-examples/bash-based/azure-pipeline.yml` 
  - path: `cicd-examples/python-based/azure-pipeline.yml`   

### Clean 

Run 
```   
make down  
```   
and it will bring down the app for you!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contributing
Contributions are welcome! Please open issues or submit pull requests.
