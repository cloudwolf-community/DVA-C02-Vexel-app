#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start flask-app
sudo systemctl enable flask-app
sudo systemctl start redis
sudo systemctl enable redis