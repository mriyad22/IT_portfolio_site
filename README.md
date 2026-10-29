# IT Solutions — Django Corporate Website

A responsive blue-white IT company website built with Django function-based views, Django templates, Bootstrap 5, custom CSS/JavaScript, and PostgreSQL.

## Features
- Home page with hero, services, portfolio, testimonials, stats and CTA
- About, services list/detail, portfolio list/detail, blog list/detail, contact, team and custom 404 pages
- Django Admin-managed services, projects, team members, testimonials, blog posts and contact messages
- Contact form validation, CSRF protection, safe ORM usage, image upload support
- PostgreSQL configuration through environment variables
- Responsive navigation and mobile-friendly layouts

## 1. Requirements
- Python 3.11+ (recommended: Python 3.12 or 3.13)
- PostgreSQL 14+
- Git (optional)

## 2. Setup (Windows PowerShell)
```powershell
cd it_company_website
py -3.12 -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edit `.env` with your PostgreSQL database details.

Create the database in PostgreSQL:
```sql
CREATE DATABASE it_company_db;
CREATE USER it_company_user WITH PASSWORD 'change-this-password';
GRANT ALL PRIVILEGES ON DATABASE it_company_db TO it_company_user;
```
For PostgreSQL 15+, also connect to `it_company_db` as a database owner and run:
```sql
GRANT ALL ON SCHEMA public TO it_company_user;
```
Or use your own database/user with the necessary privileges.

Then run:
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 3. Add website content
Sign in to Django Admin and create:
1. Service records (set `is_active=True`)
2. Project records (set `is_published=True`)
3. Team members and testimonials
4. Blog posts (set `is_published=True`)

The site includes friendly fallback content when there are no database records.

## 4. Project structure
```text
it_company_website/
├── config/
├── core/
├── services/
├── portfolio/
├── team/
├── blog/
├── contact/
├── templates/
├── static/
├── media/
├── .env.example
├── manage.py
└── requirements.txt
```

## 5. Production checklist
Before deployment:
- Set `DEBUG=False`
- Set a long, unique `SECRET_KEY`
- Configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`
- Serve static files with `collectstatic` and configure a production web server
- Store uploaded media in durable storage and back it up
- Configure HTTPS, secure cookies, database backups and email delivery
- Add rate limiting / CAPTCHA if the contact form receives spam
- Never commit `.env` or production secrets

## Notes
This is a complete starter implementation, not a claim that it has been deployed or tested against your local PostgreSQL installation. Run migrations and smoke-test it in your environment.
