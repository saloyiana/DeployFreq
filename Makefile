.PHONY: up pre-install install access clean down

up: pre-install install access

pre-install:
	@echo "Checking for updates..."
	@source pre-install.sh "example" && source pre-install.sh "Your_DB_Host"

install:
	@echo "Installing the Kubernetes resources..."
	kubectl apply -f k8s_config.yaml
	@echo "Done with the app installation."

access:
	@echo "Access the application:"
	@echo "https://$$(kubectl get ingress -n deploy-freq deployment-frequencies | awk '{print $$4}')/docs"

clean:
	@echo "Deleting the Kubernetes resources..."
	kubectl delete -f k8s_config.yaml
	@echo "Done."

down: clean