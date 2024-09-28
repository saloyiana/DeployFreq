#!/bin/bash
K8S_CONFIG_FILE="k8s_config.yaml"

if grep -q "$1" $K8S_CONFIG_FILE; then
    if [ "$1" = "Your_DB_Host" ] || [ "$1" = "example" ]; then
        echo "Make sure to update the secret or ingress host in $K8S_CONFIG_FILE"
        exit 1
    fi
else
    echo "Prerequisites checking is done!"
fi