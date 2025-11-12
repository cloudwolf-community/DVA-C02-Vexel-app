#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start flask-app
sudo systemctl enable flask-app