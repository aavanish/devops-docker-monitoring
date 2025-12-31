#!/bin/bash

RESOURCE_GROUP="devops-rg"
LOCATION="eastus"
VM_NAME="simulation-runtime-vm"
ADMIN_USER="azureuser"

echo "Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

echo "Provisioning virtual machine..."
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --image Ubuntu2204 \
  --admin-username $ADMIN_USER \
  --generate-ssh-keys \
  --size Standard_B2s

echo "Opening SSH and application ports..."
az vm open-port --resource-group $RESOURCE_GROUP --name $VM_NAME --port 22
az vm open-port --resource-group $RESOURCE_GROUP --name $VM_NAME --port 8080

echo "VM provisioning completed"

