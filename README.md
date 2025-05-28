# CI-CD-LiveApp

# 🚀 CI/CD Motivational Quotes App - Manisha

A simple **Flask-based motivational quotes app** deployed using **CI/CD pipeline (GitHub Actions) on AWS EC2**, with live updates on push to `main` branch.

---

## 🛠️ Tech Stack
- Python + Flask (Backend)
- HTML + CSS (Frontend)
- GitHub Actions (CI/CD)
- AWS EC2 (Deployment Server)
- systemd + Gunicorn (Production Server Setup)

---

## 🔄 Project Workflow

| Step | Description |
|------|-------------|
| ✅ Flask App | Displays a random motivational quote with HTML/CSS |
| ✅ GitHub | Code versioned and pushed to GitHub |
| ✅ GitHub Secrets | Added `EC2_KEY` (PEM key content) and `EC2_IP` |
| ✅ GitHub Actions | On every push to main, code is auto-deployed to EC2 |
| ✅ EC2 Setup | Installed Python, Gunicorn, setup virtualenv, systemd |
| ✅ systemd Service | Runs app in background with `flaskapp.service` |

---

## 🔧 Important Commands

```bash
# EC2 setup
sudo apt update && sudo apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn -w 3 app:app

# Systemd config (flaskapp.service)
sudo systemctl daemon-reload
sudo systemctl restart flaskapp
