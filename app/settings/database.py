# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
from os import environ

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": environ.get("DB_NAME"),
        "USER": environ.get("DB_USER"),
        "PASSWORD": environ.get("DB_PASSWORD"),
        "HOST": environ.get("DB_HOST"),
        "PORT": environ.get("DB_PORT"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}
