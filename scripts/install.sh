#!/bin/bash

sudo unzip -o /home/ec2-user/flask-app/deployment-package.zip -d /home/ec2-user/flask-app/
sudo chmod +x /home/ec2-user/flask-app/app/app.py

# Install  application dependencies
sudo pip3 install -r /home/ec2-user/flask-app/requirements.txt