# Technical_Task

🚀 **AWS CI/CD Pipeline Setup with Terraform & Jenkins**

🔑 **Prerequisites**

**1. AWS Account:**

    Access Keys: Ensure you have your Access Key ID and Secret Access Key ready.
    IAM Permissions: Grant yourself necessary permissions to create S3, RDS, ECR, Lambda, and other AWS resources.
   
**2. Jenkins Installed:**

    A running Jenkins instance on your local machine or cloud instance (e.g., AWS EC2).
   
**3. Tools Installed:**

    Terraform for provisioning AWS resources.
    Docker for containerization.
    AWS CLI for interacting with AWS services.
   
**4. Python Script Ready:**

    Ensure your app.py script is prepared to:
    Read data from S3.
    Push it to RDS or AWS Glue.

# 🛠️ Using Terraform to Set Up Resources

**🔍 Navigate to the Terraform Folder**

Inside the Terraform folder, you’ll find two key files:

    main.tf: Contains the resource setup for S3, RDS, ECR, and Lambda.
    vars.tf: Contains all required variables for resource creation.
    
If you don’t have Terraform installed, follow these steps:

Install Terraform: Terraform Installation Guide

    https://developer.hashicorp.com/terraform/install

**🚀 Terraform Commands**

Once you’re inside the Terraform folder, run the following commands to provision resources:

bash
Copy code

    terraform init
    terraform apply
These commands initialize the configuration and apply the required infrastructure setup to your AWS account.


# 🏗️ Using Jenkins for Complete CI/CD

Jenkins will handle the CI/CD pipeline for the deployment of your Lambda functions and containerized applications.

**🔧 Jenkins Setup**

Create a Jenkins Pipeline Script: Use the jenkins-pipeline file to create the pipeline.

Install Required Jenkins Plugins: Make sure to install the following plugins for a seamless CI/CD process:

    Deploy to container
    Docker Pipeline
    Pipeline and Build Tools
    AWS Integration
    Terraform Plugin
    GitHub Integration
    Utility Plugins (for convenience)

# ⚡ Step-by-Step Guide for Jenkins Pipeline Setup

1. Set up Jenkins Pipeline:

        Create a new pipeline job in Jenkins.
        Link the GitHub repository where your Terraform code and app.py script are stored.
   
2. Integrate Docker for Deployment:

        Use the Docker Pipeline plugin to manage containerized deployments.
        Configure Jenkins to build Docker images and push them to ECR for storage.
   
3. AWS Integration:

        Install the AWS Integration Plugin in Jenkins to automate deployments to AWS resources (like S3, RDS, Lambda).
   
4. Terraform Plugin:

        Integrate the Terraform Plugin to manage infrastructure provisioning directly from Jenkins. This allows you to automate the execution of terraform init and terraform apply commands.
   
# 💡 Final Notes:

Ensure you have all necessary permissions in your AWS IAM role.

Make sure your Python script is tested and ready to run.

With this setup, your CI/CD pipeline will automatically build and deploy Lambda functions, containers, and resources to AWS with minimal manual intervention.

Feel free to modify and extend the pipeline for additional features like testing, monitoring, or advanced deployment strategies!

