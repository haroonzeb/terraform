terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

provider "aws" {
  region = var.region
}

module "vpc" {
  source = "../../modules/vpc"
  cidr_block = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
  private_subnet_cidr = var.private_subnet_cidr
}

module "ec2" {
  source = "../../modules/ec2"
  vpc_id = module.vpc.vpc_id
  subnet_id = module.vpc.public_subnet_id
  instance_type = var.ec2_instance_type
}

module "rds" {
  source = "../../modules/rds"
  vpc_id = module.vpc.vpc_id
  subnet_id = module.vpc.private_subnet_id
  db_instance_class = var.rds_instance_class
  db_name = var.rds_db_name
  db_username = var.rds_db_username
  db_password = var.rds_db_password
}

module "s3" {
  source = "../../modules/s3"
  bucket_name = var.s3_bucket_name
}
