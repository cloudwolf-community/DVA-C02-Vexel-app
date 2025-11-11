#!/bin/bash
# Update OS packages
sudo yum update -y

# Ensure deployment directory exists and permissions are correct
sudo mkdir -p /home/ec2-user/flask-app
sudo chown ec2-user:ec2-user /home/ec2-user/flask-app
sudo chmod 755 /home/ec2-user/flask-app
