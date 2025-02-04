---
# Django Template Repository

This is a template repository for setting up Django projects with best practices.

## Setup

### 1. Create a Virtual Environment

Run the following command to create and activate a virtual environment:

```sh
make venv
```

### 2. Install Dependencies

After activating the virtual environment, install the required dependencies:

```sh
make install
```

### 3. Apply Migrations

Run the database migrations to set up the schema:

```sh
make migrate
```

### 4. Run the Development Server

Start the Django development server:

```sh
make start
```

### 5. Custom Management Command

This template includes a custom management command for initial setup. Run:

```sh
python manage.py initial_setup <file_path or link>
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
