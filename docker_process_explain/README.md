## 🧭 Dockerfile Flow Overview
Start from a base image (python:3.10-slim)

Set working directory to /app

Copy source code to container

Install dependencies

Expose port 8501

Run Streamlit app with the defined command





### 🔧 GitHub Actions CI/CD Workflow Explanation:
Triggered when code is pushed to the main branch.

Checks out the repo code.

Configures AWS credentials from GitHub Secrets.

Verifies AWS access and the existence of the ECR repository.

Logs in to ECR.

Builds and pushes the Docker image to ECR.

SSHs into your EC2 instance and:

Logs into ECR from EC2

Stops/removes existing container

Pulls new image

Runs updated container