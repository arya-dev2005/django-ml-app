# Django ML House Price Prediction App

A full-stack Django web application with machine learning integration, user authentication, and AWS deployment.

## Features
- 🔐 User Authentication (Signup/Login/Logout)
- 🤖 ML-powered house price predictions
- 🗄️ AWS RDS database integration
- ☁️ Deployed on AWS EC2
- 📱 Responsive design

## Tech Stack
- **Backend:** Django 5.0
- **ML:** Scikit-learn, Linear Regression
- **Database:** MySQL (AWS RDS) / SQLite (local)
- **Deployment:** AWS EC2
- **Version Control:** Git & GitHub

## Local Setup

1. Clone repository:
```bash
git clone https://github.com/YOUR_USERNAME/django-ml-app.git
cd django-ml-app
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run server:
```bash
python manage.py runserver
```

7. Visit: `http://127.0.0.1:8000`

## Model Info
- **Type:** Linear Regression
- **Input:** House area (sq ft)
- **Output:** Predicted price ($)

## Author
Your Name