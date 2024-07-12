variable "region" {
  description = "The AWS region to deploy the infrastructure"
  type = string
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  type = string
}

variable "public_subnet_cidr" {
  description = "The CIDR block for the public subnet"
  type = string
}

variable "private_subnet_cidr" {
  description = "The CIDR block for the private subnet"
  type = string
}

variable "ec2_instance_type" {
  description = "The instance type for the EC2 instances"
  type = string
}

variable "rds_instance_class" {
  description = "The instance class for the RDS instance"
  type = string
}

variable "rds_db_name" {
  description = "The name of the RDS database"
  type = string
}

variable "rds_db_username" {
  description = "The username for the RDS database"
  type = string
}

variable "rds_db_password" {
  description = "The password for the RDS database"
  type = string
  sensitive = true
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket"
  type = string
}
