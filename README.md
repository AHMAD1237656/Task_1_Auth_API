# Authentication & User Management API

## Overview

This project is a Django REST Framework based Authentication API developed as an internship task.

## Features

- User Registration
- JWT Authentication
- Login
- Refresh Token
- User Profile
- Update Profile
- Change Password
- Forgot Password
- Reset Password
- Email Verification
- Role Based Access Control (RBAC)
- Rate Limiting
- PostgreSQL Integration
- Swagger API Documentation

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- drf-spectacular

## Installation

```bash
git clone <repository-url>

cd Task_1_Auth_API

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## API Documentation

```
http://127.0.0.1:8000/api/docs/
```

## Author

Ahmed Jutt