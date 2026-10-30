<div align="center">

# IT Solutions — Corporate Website

A responsive IT company website built with **Django**, **Bootstrap 5**, **HTML**, **CSS** and **JavaScript**.

[![Live Preview](https://img.shields.io/badge/Live%20Preview-Visit%20Website-2563EB?style=for-the-badge&logo=googlechrome&logoColor=white)](https://it.pybrothers.top/)



</div>

---

## Live Preview

Explore the deployed website:

👉 **[🌐 View Live Website](https://it.pybrothers.top/)**

> The live preview opens the hosted website in your browser. The source code and local setup instructions are provided below.

## About the Project

This project is a dynamic corporate website for an IT solutions company. It presents company information, services, portfolio projects, team members, client testimonials, and blog/insight articles. Website content can be managed through Django's admin panel and a custom staff dashboard.

## Features

- **Home page** — hero section, services, featured projects, testimonials, latest insights and calls to action.
- **About page** — company introduction.
- **Services** — service listing and individual service detail pages.
- **Portfolio** — project listing, project details and category-based filtering.
- **Team** — team member profiles.
- **Testimonials** — client reviews and ratings displayed on the home page.
- **Insights / Blog** — published article listing and detail pages.
- **Contact** — validated contact form with a hidden honeypot field for basic bot filtering.
- **Image uploads** — support for service, project, team, testimonial and blog images.
- **Responsive interface** — Bootstrap 5 with custom CSS and JavaScript.
- **Custom 404 page** — branded not-found page.

## Technology Stack

| Area | Technology |
|---|---|
| Backend | Python, Django 5.2 |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Database | PostgreSQL |
| Static files | WhiteNoise |
| Image handling | Pillow |
| Environment variables | python-dotenv |

## Project Structure

```text
.
├── config/                 # Django project settings, URLs, ASGI and WSGI
├── core/                   # Home and About pages
├── services/               # Service models, views and admin
├── portfolio/              # Project and project-category management
├── team/                   # Team members and testimonials
├── blog/                   # Insights / blog posts
├── contact/                # Contact form and message records
├── templates/              # Shared and app-specific Django templates
├── static/
│   ├── css/
│   └── js/
├── media/                  # Uploaded media (created when needed)
├── manage.py
└── requirements.txt
```

## Getting Started

### 1. Requirements

- Python 3.11 or newer
- pip
- Git (optional)

The project's current settings use SQLite by default, so PostgreSQL is not required to run the project locally.

### 2. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
```

If you downloaded the source as a ZIP file, extract it and open a terminal in the project directory.

### 3. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email and password.

### 7. Run the development server

```bash
python manage.py runserver
```

Open these URLs:

| Page | URL |
|---|---|
| Website | http://127.0.0.1:8000/ |
| Services | http://127.0.0.1:8000/services/ |
| Portfolio | http://127.0.0.1:8000/projects/ |
| Team | http://127.0.0.1:8000/team/ |
| Insights | http://127.0.0.1:8000/insights/ |
| Contact | http://127.0.0.1:8000/contact/ |

The custom dashboard requires an authenticated user with `is_staff=True`.


---

<div align="center">

**Live Website:** [it.pybrothers.top](https://it.pybrothers.top/)

Built with Django by @mriyad22

</div>
