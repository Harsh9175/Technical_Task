provider "aws" {
  region = "us-east-1"
}

# S3-Bucket
resource "aws_s3_bucket" "data_bucket" {
  bucket = var.s3_bucket_name
}

# RDS MySQL Instance
resource "aws_db_instance" "db_instance" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  # name                 = "data_db"
  username             = var.db_username
  password             = var.db_password
  publicly_accessible  = true
  skip_final_snapshot = true
}

# ECR Repository
resource "aws_ecr_repository" "docker_repo" {
  name = var.ecr_repo_name
}
