import os

from config import Config
from .base import *


# === Application settings ===
DEBUG = False

SECRET_KEY = Config.get("prod")["secret_key"]

ALLOWED_HOSTS = [ Config.get("prod")["base_url"] ]
CSRF_TRUSTED_ORIGINS = [ "https://" + Config.get("prod")["base_url"] ]

MEDIA_ROOT = os.getenv('CODERDOJO_PORTAL_STORAGE', os.path.join(BASE_DIR, "media"))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# === Database settings ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": Config.get("prod")["database"]["name"],
        "USER": Config.get("prod")["database"]["user"],
        "PASSWORD": Config.get("prod")["database"]["password"],
        "HOST": Config.get("prod")["database"]["host"],
        "PORT": Config.get("prod")["database"]["port"],
    }
}


# === Email settings ===
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# === Wagtail settings ===
#
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "https://" + Config.get("prod")["base_url"]
