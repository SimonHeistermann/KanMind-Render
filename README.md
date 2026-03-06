# KanMind

> A modern Kanban board web application with Django REST backend and responsive frontend — training project from Developer Akademie.

---

## Disclaimer

This is a **training/portfolio project** built as part of my education at [Developer Akademie](https://developerakademie.com/). It is **not** a commercial product and is not intended for real-world use.

- No real transactions, orders, or services are processed
- This is a demo application — do not enter real personal data
- Any resemblance to real businesses is for educational demonstration only

**Note:** I built the **backend** for this project. The frontend was provided as part of the Developer Akademie curriculum.

> Looking for the **backend-only** version (submitted as the backend assignment)? See [KanMind (Backend)](https://github.com/SimonHeistermann/KanMind).

---

## About

KanMind is a Kanban board tool that helps teams and individuals organize tasks efficiently. It features an intuitive board system with role-based permissions, task workflows with assignment and review flows, and secure token-based authentication via Django REST Framework.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django 5.2 + Django REST Framework |
| **Auth** | Django User + Token Authentication |
| **DB** | SQLite (dev) / PostgreSQL (prod) |
| **Env Management** | `.env` / `env-template` |

---

## Features

- Intuitive Kanban Board with customizable columns (To Do, In Progress, Review, Done)
- User Roles: Guest, User, Admin with different permissions
- Task Management: Create, edit, and track task status
- Task Assignment & review flows
- Comment System for task communication
- Secure Backend using Django REST Framework + Token Authentication
- Responsive Frontend (HTML, CSS, JS)
- CORS-ready for local development & production deployment

---

## Getting Started

### Prerequisites

- **Python 3.13+**
- **pip** (Python package manager)
- **(Optional)** Virtual Environment (`venv`)
- **Git**
- **Frontend-Live-Server** (e.g. VSCode Live Server Extension)

### 1. Clone the Repository
```bash
git clone https://github.com/SimonHeistermann/KanMind-Render.git
cd KanMind-Render
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
```bash
cp env-template .env # macOS / Linux
# or
copy env-template .env # Windows (Command Prompt)
```
Tip: Never commit your .env file to Git.
You can safely use the default values for local development.
Optionally, replace SECRET_KEY or toggle DEBUG.

### 5. Generate your own SECRET_KEY
Django requires a secret key for cryptographic signing.
You must generate one manually and add it to your .env file.

Option 1 (recommended):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the generated key into your .env file:
```bash
SECRET_KEY='your-secret-key-here'
```

Option 2:
If Django isn't installed yet, use an online generator such as https://djecrety.ir/ and paste the result into your .env.

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create a Superuser
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

Open in browser: http://127.0.0.1:8000/

### 9. Create Guest User for Guest Login

Log into the admin page of the project and create a guest user with the following information:

| Field       | Value                |
|-------------|----------------------|
| **Username** | guest@guest.de      |
| **Email**    | guest@guest.de      |
| **Password** | o6B6<c1x\|`N2        |
| **First Name** | Guest             |
| **Last Name**  | User              |

---

## Hosting / Production Setup

If you plan to host your project (e.g. on Render, Railway, or your own VPS/server):

### Update your .env file

```
DEBUG=False
SECRET_KEY=<your-production-secret>
ALLOWED_HOSTS=kanmind.yourdomain.com
DATABASE_URL=postgres://user:pass@host:port/dbname
CORS_ALLOWED_ORIGINS=https://kanmind.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://kanmind.yourdomain.com
```

### Collect static files
```bash
python manage.py collectstatic
```

### Configure Gunicorn + Reverse Proxy (e.g. Nginx)

Set up Gunicorn as your WSGI server and use Nginx to serve static files and handle HTTPS requests.

Example (conceptually):

Gunicorn listens on 127.0.0.1:8000

Nginx listens on port 80/443 and proxies requests to Gunicorn

### SSL Certificates

Use Let's Encrypt (via Certbot) to enable HTTPS.

### Debugging Tips

If you get 403 Forbidden errors:

Check your Browser DevTools → Network tab → Ensure the request includes the header:

`Authorization: Token <YOUR_TOKEN>`

Guest users don't need admin rights, but they must be authenticated (valid token present).

Remember: Django only loads .env values when the server starts, so after editing your .env, restart it:
```bash
python manage.py runserver
```

---

## Project Structure

```
KanMind-Render/
├── backend/          # The complete backend
├── frontend/         # The complete frontend
├── .gitignore
└── README.md
```

---

## Related Repositories

| Repository | Description |
|------------|-------------|
| [KanMind-Render](https://github.com/SimonHeistermann/KanMind-Render) | Full project (frontend + backend), deployed on Render |
| [KanMind](https://github.com/SimonHeistermann/KanMind) | Backend-only version (Developer Akademie backend assignment) |

---

## Legal

- [Impressum / Legal Notice](frontend/pages/imprint/index.html)
- [Privacy Policy](frontend/pages/privacy/index.html)

---

## Author

**Simon Maximilian Heistermann**
- Website: [simon-heistermann.de](https://simon-heistermann.de)
- Email: simon@heistermann-solutions.de
- LinkedIn: [Simon Heistermann](https://www.linkedin.com/in/simon-heistermann/)

---

## License

This project is part of a training curriculum and is not licensed for commercial use.
