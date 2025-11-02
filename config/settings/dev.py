from .base import *
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


DEBUG = True
ALLOWED_HOSTS = ["*"]

# INSTALLED_APPS += ["django_filters",
# ]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]

DATABASES["default"]["HOST"] = "localhost"
DATABASES["default"]["PORT"] = "5432"
DATABASES["default"]["USER"] = "postgres"
DATABASES["default"]["PASSWORD"] = "Rushikesh@97"
DATABASES["default"]["NAME"] = "photography_db"
