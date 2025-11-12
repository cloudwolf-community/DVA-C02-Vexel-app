#!/bin/bash

# Copy systemd unit file 
sudo cp /home/ec2-user/flask-app/scripts/flask-app.service /etc/systemd/system/flask-app.service
sudo chmod 644 /etc/systemd/system/flask-app.service

# Reload systemd to recognize new service 
sudo systemctl daemon-reload
