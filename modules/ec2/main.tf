resource "aws_instance" "main" {
  ami           = "ami-0c55b159cbfafe1f0" # Example AMI ID
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  tags = {
    Name = "main_instance"
  }
}
