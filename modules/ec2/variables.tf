variable "instance_type" {
  description = "The instance type for the EC2 instances"
  type = string
}

variable "subnet_id" {
  description = "The subnet ID where the instance will be deployed"
  type = string
}
