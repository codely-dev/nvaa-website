from .base import *

DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")

CSRF_TRUSTED_ORIGINS = ['https://nvaa.ch']

try:
    from .local import *
except ImportError:
    pass

# Database
APP_URL = 'nvaa.ch'
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nvaa',
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'nvaa.ch'