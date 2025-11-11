#!/bin/bash

# Update OS packages
sudo yum update -y

# Update system
sudo dnf update -y

# Install Python 3.11 (latest available)
sudo dnf install python3.11 python3.11-pip -y

# Install pip if not included
sudo python3 -m ensurepip --upgrade

# Create symlink if needed
sudo ln -sf /usr/bin/python3.11 /usr/bin/python3

# Ensure deployment directory exists and permissions are correct
sudo mkdir -p /home/ec2-user/flask-app
sudo chown ec2-user:ec2-user /home/ec2-user/flask-app
sudo chmod 755 /home/ec2-user/flask-app