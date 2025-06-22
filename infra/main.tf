resource "aws_security_group" "mlops_sg" {
  name        = "mlops-sg"
  description = "Allow SSH, HTTP and custom ports"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "mlops_api" {
  ami                    = "ami-04b70fa74e45c3917" # Amazon Linux 2 us-east-1 (à vérifier)
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.mlops_sg.id]
  tags = {
    Name = "mlops-api"
  }
}

resource "aws_instance" "mlops_training" {
  ami                    = "ami-04b70fa74e45c3917"
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.mlops_sg.id]
  tags = {
    Name = "mlops-training"
  }
}
