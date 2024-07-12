variable "db_instance_class" {
  description = "The instance class for the RDS instance"
  type = string
}

variable "db_name" {
  description = "The name of the RDS database"
  type = string
}

variable "db_username" {
  description = "The username for the RDS database"
  type = string
}

variable "db_password" {
  description = "The password for the RDS database"
  type = string
  sensitive = true
}

variable "subnet_id" {
  description = "The subnet ID for the RDS instance"
  type = string
}
