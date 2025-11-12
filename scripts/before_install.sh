#!/bin/bash

# Update OS packages
sudo yum update -y

# Install Redis server
sudo yum install -y redis

# Update system
sudo dnf update -y

# Install Python 3.11 (latest available)
sudo dnf install python3.11 python3.11-pip -y

# Install pip if not included
python3 -m ensurepip --upgrade

# Create symlink if needed
sudo ln -sf /usr/bin/python3.11 /usr/bin/python3
sudo ln -sf /usr/lib/python3.11/site-packages/pip /usr/bin/pip

# Ensure deployment directory exists 
sudo mkdir -p /home/ec2-user/flask-app
sudo chown ec2-user:ec2-user /home/ec2-user/flask-app