# Shorty

URL shortener application built with Django and PostgreSQL.

## Installation Guide

Follow steps to install locally.

1. Prerequisites
    Python 3.8+
    PostgreSQL
    Git

2. Clone Repository

```bash
git clone <repo-url>
cd url_shortener_project

```

3. Setup Database

```bash
sudo -iu postgres psql
CREATE USER your_db_user WITH PASSWORD 'password123';
CREATE DATABASE shortener_db OWNER your_db_user;
\q

```

4. Configure Environment Variables

```bash
cp .env.example .env
```

open the .env file and set the following variables:

SECRET_KEY='generate-a-strong-random-key-here'
DEBUG=True
DATABASE_URL='postgres://your_db_user:your_password@localhost:5432/shortener_db'

5. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

6. Install Dependencies

```bash
pip install -r requirements.txt
```

7. Run Database Migrations

```bash
python manage.py migrate
```

8. Create Superuser (Optional)
For django admin panel

```bash
python manage.py createsuperuser
```

9. Run Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/.



