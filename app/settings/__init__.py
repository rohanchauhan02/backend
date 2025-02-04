"""
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ
from split_settings.tools import include

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "common.py",
    "database.py",
]

if ENV == "production":
    base_settings.append("production.py")

# Include settings:
include(*base_settings)
