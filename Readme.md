# Django Template Repository

This is a template repository for setting up Django projects with best practices.

## Setup

### 1. Create a Virtual Environment

Run the following command to create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

After activating the virtual environment, install the required dependencies:

```sh
pip install -r requirements.txt
```

### 3. Apply Migrations

Run the database migrations to set up the schema:

```sh
python manage.py migrate
```

### 4. Run the Development Server

Start the Django development server:

```sh
python manage.py runserver
```

### 5. Custom Management Command

This template includes a custom management command for initial setup. Run:

```sh
python manage.py initial-setup
```

### 6. Creating a Superuser

To access the Django Admin panel, create a superuser:

```sh
python manage.py createsuperuser
```

### 7. Environment Variables

Copy `.env.example` to `.env` and configure your environment variables:

```sh
cp .env.example .env
```

### 8. API Endpoints

This project includes CRUD APIs. You can test them using Postman or cURL.

---

Would you like me to include additional sections, such as Docker setup, deployment instructions, or testing guidelines? 🚀
