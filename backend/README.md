# 🗂️ KanMind

**KanMind** is a modern, user-friendly Kanban tool that helps teams and individuals organize tasks efficiently.
It combines an intuitive board system with role management, task workflows, and secure user authentication via Django REST Framework.

---

## 🚀 Features

- 🧱 **Intuitive Kanban Board** with customizable columns (To Do, In Progress, Review, Done)
- 👥 **User Roles**: Guest, User, Admin with different permissions
- ✅ **Task Management**: Create, edit, and track task status
- 🔄 **Task Assignment** & review flows
- 💬 **Comment System** for task communication
- 🔐 **Secure Backend** using Django REST Framework + Token Authentication
- 📱 **Responsive Frontend** (HTML, CSS, JS)
- 🌐 **CORS-ready** for local development & production deployment

---

## 🧠 Tech Stack

| Bereich | Technologie |
|----------|--------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django 5.2 + Django REST Framework |
| **Auth** | Django-User + Token-Auth |
| **DB** | SQLite (dev) / PostgreSQL (prod möglich) |
| **Env Management** | `.env` / `env-template` |

---

## 📦 Voraussetzungen

- **Python 3.13+**
- **pip** (Python package manager)
- **(Optional)** Virtual Environment (`venv`)
- **Git**
- **Frontend-Live-Server** (z. B. VSCode Live Server Extension)

---

## 🛠️ Setup (Development)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SimonHeistermann/DA-KanMind.git
cd DA-KanMind
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Setup
```bash
cp env-template .env # macOS / Linux
# or
copy env-template .env # Windows (Command Prompt)
```
🔐 Tip: Never commit your .env file to Git.
You can safely use the default values for local development.
Optionally, replace SECRET_KEY or toggle DEBUG.

### 5️⃣ 🔑 Generate your own SECRET_KEY
Django requires a secret key for cryptographic signing.
You must generate one manually and add it to your .env file.

Option 1 (recommended):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the generated key into your .env file:
```bash
SECRET_KEY=your-secret-key-here
```

Option 2:
If Django isn’t installed yet, use an online generator such as
👉 https://djecrety.ir/

and paste the result into your .env.

### 6️⃣ Run Migrations
```bash
python manage.py migrate
```

### 7️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 8️⃣ Run the Development Server
```bash
python manage.py runserver
```

--> Open in browser:
➡️ http://127.0.0.1:8000/

### 9️⃣ Create Guest User for Guest Login

Log into the admin page of the project and create a guest user with the following information:

| Field       | Value                |
|-------------|----------------------|
| **Username** | guest@guest.de      |
| **Email**    | guest@guest.de      |
| **Password** | o6B6<c1x|`N2        |
| **First Name** | Guest             |
| **Last Name**  | User              |

---

## 🌐 Hosting / Production Setup

If you plan to host your project (e.g. on Render, Railway, or your own VPS/server):

### 🔧 Update your .env file

DEBUG=False
SECRET_KEY=<your-production-secret>
ALLOWED_HOSTS=kanmind.yourdomain.com
DATABASE_URL=postgres://user:pass@host:port/dbname
CORS_ALLOWED_ORIGINS=https://kanmind.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://kanmind.yourdomain.com

### 📦 Collect static files
```bash
python manage.py collectstatic
```

### ⚙️ Configure Gunicorn + Reverse Proxy (e.g. Nginx)

Set up Gunicorn as your WSGI server and use Nginx to serve static files and handle HTTPS requests.

Example (conceptually):

Gunicorn listens on 127.0.0.1:8000

Nginx listens on port 80/443 and proxies requests to Gunicorn

### 🔒 SSL Certificates

Use Let’s Encrypt (via Certbot) to enable HTTPS.

### 🧰 Debugging Tips

If you get 403 Forbidden errors:

Check your Browser DevTools → Network tab
→ Ensure the request includes the header:

Authorization: Token <YOUR_TOKEN>

--> Guest users don’t need admin rights, but they must be authenticated (valid token present).

Remember:
👉 Django only loads .env values when the server starts, so after editing your .env, restart it:
```bash
python manage.py runserver
```

### 📁 Project Structure
```bash
DA-KanMind/
│
├── core/                  # Django core config (settings, urls, wsgi)
├── dashboard_app/         # Kanban boards & tasks API
├── user_auth_app/         # Registration, login, token auth
├── frontend/              # Frontend (HTML, CSS, JS)
├── env-template           # Environment variable template
├── requirements.txt       # Dependencies
└── manage.py
```

### 🧩 License

MIT License © 2025 Simon Heistermann