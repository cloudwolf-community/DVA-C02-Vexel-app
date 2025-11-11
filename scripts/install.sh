#!/bin/bash

unzip -o /home/ec2-user/flask-app/deployment-package.zip -d /home/ec2-user/flask-app/
chmod +x /home/ec2-user/flask-app/app/app.py

# Install  application dependencies
python3 -m pip install -r /home/ec2-user/flask-app/requirements.txt