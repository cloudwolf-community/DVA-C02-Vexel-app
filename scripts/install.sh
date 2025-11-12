#!/bin/bash

sudo chmod +x /home/ec2-user/flask-app/app/app.py

# Install  application dependencies
python3 -m pip install -r /home/ec2-user/flask-app/requirements.txt