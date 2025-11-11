# Flask EC2 Deployment Tutorial

This project demonstrates a complete CI/CD pipeline for deploying a Python Flask application to EC2 instances using AWS CodeBuild, CodeDeploy, and CodePipeline.

It is designed as a tutorial example for learners preparing for the AWS Developer Associate (DVA-C02) exam to understand real-world server-based deployment lifecycle.

---

## Features

- Simple Python 3.13 Flask web application with basic order processing API
- Automated dependency installation and testing in CodeBuild
- Packaging and deployment artifact creation in CodeBuild
- CodeDeploy lifecycle hooks to manage the application service on EC2 using systemd
- Automated creation, start, stop, and validation of the Flask service on EC2
- Health check validation using HTTP requests to ensure successful deployment

---

## File Structure

### /app
- app.py # Flask app code
### /scripts
- stop_server.sh # Stop systemd service script
- before_install.sh # Pre-install update script
- after_install.sh # Unpack deployment package script
- start_server.sh # Start systemd service script
- validate.sh # HTTP health check script
- setup_systemd.sh # (Optional) Setup systemd service unit script
- flask-app.service # systemd service unit file

### /static_src
- style.scss

### /
- appspec.yml # CodeDeploy deployment spec file
- buildspec.yml # CodeBuild build spec file
- requirements.txt # Python dependencies (Flask pinned version)
- README.md # This file

---

## Setup & Deployment Instructions

### Prerequisites

- AWS CLI configured with correct permissions
- EC2 instances running Amazon Linux 2 with IAM role for CodeDeploy
- IAM Roles setup for CodeBuild, CodeDeploy, and CodePipeline
- GitHub repository with this code connected to CodePipeline

### EC2 Instance Configuration

1. Install dependencies on EC2:

sudo yum update -y
sudo yum install -y python3 unzip aws-codedeploy-agent
sudo alternatives --install /usr/bin/python python /usr/bin/python3.13 1
sudo systemctl start codedeploy-agent
sudo systemctl enable codedeploy-agent

2. Create `flask-app.service` in `/etc/systemd/system/` manually or automate using the provided `setup_systemd.sh` script in lifecycle hooks.

3. Reload systemd:

sudo systemctl daemon-reload

---

### Pipeline Setup

- **Source:** Connect CodePipeline to your GitHub repo.
- **Build:** Define CodeBuild project that uses `buildspec.yml`.
- **Deploy:** Configure CodeDeploy application and deployment groups targeting your EC2 instances.

---

### Running the Pipeline

- Commits to GitHub trigger CodePipeline.
- CodeBuild installs dependencies, runs simple HTTP check, then packages the app.
- CodeDeploy deploys the app to EC2, manages service start/stop, and validates deployment via health check.
- Successful pipelines update the Flask app on EC2 with zero downtime ensured by lifecycle hooks.

---

## Notes

- `requirements.txt` only includes `Flask==2.3.2` as `jsonify` and `request` are part of Flask.
- Lifecycle hooks in `appspec.yml` handle app stop, install, start and validation cleanly.
- Using `systemd` for service management provides robustness beyond simple process scripts.