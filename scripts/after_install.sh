#!/bin/bash

# Make the app executable
sudo chmod +x /home/ec2-user/flask-app/app/app.py

# Install  application dependencies
sudo python3 -m pip install -r /home/ec2-user/flask-app/requirements.txt

# Copy systemd unit file
sudo cp /home/ec2-user/flask-app/scripts/flask-app.service /etc/systemd/system/flask-app.service
sudo chmod 644 /etc/systemd/system/flask-app.service

# Reload systemd to recognize new service
sudo systemctl daemon-reload
