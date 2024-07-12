resource "aws_vpc" "main" {
  cidr_block = var.cidr_block

  tags = {
    Name = "main_vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.public_subnet_cidr
  map_public_ip_on_launch = true

  tags = {
    Name = "public_subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = var.private_subnet_cidr

  tags = {
    Name = "private_subnet"
  }
}

modules/vpc/variables.tf
variable "cidr_block" {
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
