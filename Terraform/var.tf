variable "s3_bucket_name" {
  default = "data-processing-bucket-21-12-2024"
}

variable "db_username" {
  default = "admin"
}

variable "db_password" {
  default = "securepassword123"
}

variable "ecr_repo_name" {
  default = "data-processing-app"
}

variable "lambda_function_name" {
  default = "data-processing-lambda"
}
