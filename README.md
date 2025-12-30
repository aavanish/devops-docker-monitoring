# End-to-End DevOps Project: CI/CD, Docker, Azure & Monitoring

## Project Overview
This project demonstrates a *complete end-to-end DevOps workflow* starting from local development to production-like deployment and monitoring on Azure infrastructure.
The goal of this project is to showcase *real-world DevOps practices* such as:
- CI/CD automation
- Containerization
- Cloud infrastructure provisioning
- Simulation workload execution
- Monitoring & observability

This project was built as part of **DevOps interview preparation** and reflects production-oriented thinking rather than a simple demo.
---
## Problem Statement
Modern applications require:
- Automated build and deployment pipelines
- Portable containerized workloads
- Scalable cloud infrastructure
- Continuous monitoring and visibility

This project simulates a **containerized simulation/analysis job** that is:
- Automatically built via CI/CD
- Deployed on Azure VMs
- Continuously monitored using open-source tools
---
## Tech Stack

| Category            | Tools Used |
|---------------------|-----------|
| Version Control     | Git, GitHub |
| CI/CD               | Azure DevOps Pipelines |
| Containerization    | Docker |
| Container Registry  | DockerHub, Azure Container Registry (ACR) |
| Cloud Platform      | Microsoft Azure |
| Compute             | Azure Virtual Machines |
| Scripting           | Bash |
| Monitoring          | Prometheus, Grafana, cAdvisor |
| Language            | Python |

---

## Repository Structure

---

## CI/CD Pipeline Flow

### 1️⃣ Code Commit
- Developer commits code to GitHub
- Push to `main` branch triggers Azure DevOps pipeline automatically

### 2️⃣ Build Stage
- Docker image is built using `Dockerfile`
- Application dependencies installed
- Image tagged with version

### 3️⃣ Push to Registries
- Image pushed to **DockerHub**
- Image pushed to **Azure Container Registry (ACR)**

### 4️⃣ Deployment
- Azure VM created using Azure CLI script
- Docker installed on VM
- Container pulled and executed on VM

---

## Dockerized Simulation Job

### Simulation Description
The Python application simulates a **long-running analysis job**, producing logs and consuming CPU/memory to generate meaningful monitoring metrics.

### Sample Output

---

## Azure Infrastructure Automation

### Azure VM Creation
VMs are provisioned using **Azure CLI scripts**, ensuring repeatable and automated infrastructure setup.

Key Features:
- Resource Group creation
- Ubuntu VM provisioning
- SSH-based access
- Docker runtime installation

---

## Monitoring & Observability

### Monitoring Stack
- **Prometheus** – Metrics collection
- **cAdvisor** – Container-level metrics
- **Node Exporter** – VM metrics
- **Grafana** – Visualization dashboards

### Metrics Observed
- CPU utilization
- Memory usage
- Container uptime
- Resource spikes during simulation execution

This provides **real-time visibility** into both infrastructure and application behavior.

---

##  You could run it locally -- 

```bash
git clone https://github.com/aavanish/devops-docker-monitoring.git
cd devops-docker-monitoring

docker build -t devops-simulation .
docker run devops-simulation





