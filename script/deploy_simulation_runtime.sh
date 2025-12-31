#!/bin/bash

VM_IP=$1
IMAGE_NAME="aavanish/batch-simulation-engine:latest"

if [ -z "$VM_IP" ]; then
  echo "Usage: ./deploy_simulation_runtime.sh <VM_PUBLIC_IP>"
  exit 1
fi

ssh azureuser@$VM_IP << EOF
  sudo apt update -y
  sudo apt install -y docker.io
  sudo systemctl start docker
  sudo systemctl enable docker

  sudo docker pull $IMAGE_NAME
  sudo docker run -d --name batch-simulation-engine $IMAGE_NAME
EOF

