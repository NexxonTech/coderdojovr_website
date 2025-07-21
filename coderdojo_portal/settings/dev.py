import os

from .base import *
from config import Config


# === Application settings ===
DEBUG = True

SECRET_KEY = Config.get("dev")["secret_key"]

ALLOWED_HOSTS = ["*"]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# === Database settings ===
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# === Email settings ===
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# === Wagtail settings ===
#
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://localhost:8000"
