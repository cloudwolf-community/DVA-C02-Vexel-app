#!/bin/bash
# Update OS packages
sudo yum update -y

# Ensure deployment directory exists and permissions are correct
mkdir -p /home/ec2-user/flask-app
chown ec2-user:ec2-user /home/ec2-user/flask-app
chmod 755 /home/ec2-user/flask-app
