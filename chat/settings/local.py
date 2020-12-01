from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chatdb',
        'USER': 'solid',
        'PASSWORD': '1122',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [
            os.path.join(BASE_DIR, '../static')
]