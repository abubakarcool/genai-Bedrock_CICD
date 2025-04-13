Amazon Bedrock is a fully managed cloud service by AWS that lets you build and deploy generative AI applications using foundation models from top AI companies — without managing any infrastructure.
 
### search Bedrock and get start and request model request for first time
### create envirnment and activate it and then install the requirements
```
conda create -n llmops python=3.8 -y
conda activate llmops
pip install -r requirements.txt
```
### search IAM(identity access management) and create user and give permission of bedrock to it 
### create user -> name and next -> attach policy and AmazonBedrockFullAccess and check it and create user
### to get the API key click on created user and click security credentials and create access key and check command line interface CLI and click next and create the access key. download the csv file.
### next we need to configure it, download AWS cli and install it
```
aws configure
```
## give the access key and secret key and also the location as ap-south-1

```
streamlit run .\main.py
```


### For CI/CD DOCKER 
# 🚀 Streamlit + AWS Bedrock CI/CD Deployment Guide

This guide helps you deploy a **Streamlit** app integrated with **AWS Bedrock** using **GitHub Actions**, **ECR**, and **EC2**. It supports automatic deployment every time you push to your GitHub repository. 🔁

---

## 🛠️ Prerequisites

- GitHub account
- AWS account
- Basic knowledge of Git and terminal
- Streamlit project ready locally

---

## 📦 Step-by-Step Setup

### 1. ✅ Create an IAM User in AWS

- Go to **IAM** in AWS Console.
- Create a new user: `test_aws`.
- Select **Access key – Programmatic access**.
- Attach the following policies:
  - `AmazonEC2FullAccess`
  - `AmazonECRFullAccess`
  - `IAMUserChangePassword`
- After creation, **download credentials** (Access Key & Secret Key).

---

### 2. 🐳 Create a Docker Repository (ECR)

- Go to **ECR** in AWS Console.
- Region: `ap-south-1`
- Click **Create Repository**:
  - Name: `test-aws`
  - Settings: default
- Copy the **repository URI** for later use.

---

### 3. 🖥️ Launch an EC2 Instance

- Go to **EC2** → Launch Instance:
  - Name: `test_aws`
  - OS: Ubuntu
  - Type: t2.medium (8GB RAM)
  - Create a new key pair:
    - Name: `test-aws`
    - Format: `.pem`, RSA
- Launch the instance.
- When it’s **running**, click **Connect** → open the terminal (SSH).

---

### 4. 🐧 Install Docker on EC2

Paste the following commands in the EC2 terminal:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
### 5. 📁 Push Project to GitHub
In your local terminal (VS Code):
```bash
git add .
git commit -m "first commit of ci/cd"
git push origin main
```

### 6. ⚙️ Set Up GitHub Actions Runner (Self-Hosted)
Go to GitHub Repo → Settings → Actions → Runners

Click New self-hosted runner

Select:

OS: Linux

Architecture: x64

Follow the instructions and run the commands in EC2 terminal.

When asked for the runner name, enter: self-hosted

Finish setup with:
```bash
./run.sh
```

### 7. ☁️ Install AWS CLI on EC2 (if not installed)
Check version:

```bash
aws --version
```
If not installed:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### 8. 🔐 Add GitHub Secrets
Go to GitHub → Settings → Secrets and Variables → Actions, then add:

Name	Value
AWS_ACCESS_KEY_ID	            From IAM user
AWS_SECRET_ACCESS_KEY	        From IAM user
AWS_DEFAULT_REGION	            ap-south-1
ECR_REPO	                    test-aws
EC2_HOST	                    EC2 Public IPv4 DNS
EC2_SSH_KEY	                    Paste full content of .pem file

### 9. 🤖 Trigger CI/CD by Pushing
In your local terminal:
```bash
git add .
git commit -m "trigger deployment"
git push origin main
```
Then go to GitHub → Actions tab and monitor the deployment workflow.

10. 🔓 Open Port 8501 in EC2
To access the Streamlit app:

Go to EC2 Console

Click your instance → Security

Click the Security Group → Edit inbound rules

Add Rule:
    Type: Custom TCP
    Port Range: 8501
    Source: 0.0.0.0/0
    Save the rule

Now open in your browser:
```
http://<YOUR_EC2_PUBLIC_IP>:8501
```
You should see your Streamlit app! 🎉

### 11. ♻️ Continuous Deployment
Any time you make code changes locally:
```bash
git commit -am "update"
git push origin main
```
GitHub Actions will auto-build and deploy your Docker image to EC2 via ECR.









## 🧹 Stopping & Deleting AWS Resources (To Avoid Billing)

Once you're done testing or running your project, it's important to clean up all AWS resources to **prevent any ongoing charges**. Here's how to stop and remove everything used in this setup:

---

### 🖥️ 1. Terminate EC2 Instance

1. Go to the **EC2 Dashboard**.
2. Click **Instances** from the left sidebar.
3. Select your instance (e.g., `test_aws`).
4. Click the **"Instance state"** dropdown.
5. Choose **Terminate instance**.
6. Confirm when prompted.

💡 **Note:** This will **delete the instance** permanently (including any Docker containers and code on it).

---

### 🧱 2. Delete ECR Images and Repository

1. Go to the **ECR Console**.
2. Select your repository (e.g., `test-aws`).
3. Click **"View images"**.
4. Select all images → Click **"Delete"** → Confirm.
5. Go back to the repository list.
6. Select your repository again → Click **"Delete repository"** → Confirm.

🛑 Images stored in ECR **can incur charges**, so deleting them is critical.

---

### 🧑‍💼 3. Delete the IAM User

1. Go to the **IAM Dashboard**.
2. Click **Users** in the sidebar.
3. Find the IAM user you created (e.g., `test_aws`).
4. Click the username.
5. Under the **Security Credentials** tab:
   - Revoke and delete **access keys**.
6. Click **"Delete user"** at the top right → Confirm.

✅ This removes AWS programmatic access (used in GitHub Actions).

---

### ✅ That’s it! You're now fully cleaned up and won’t be billed further.

🧠 **Tip:** Always review your AWS billing dashboard to double-check there’s no active resource left.



