output "api_instance_ip" {
  description = "Public IP of the API instance"
  value       = aws_instance.mlops_api.public_ip
}

output "training_instance_ip" {
  description = "Public IP of the training instance"
  value       = aws_instance.mlops_training.public_ip
}
