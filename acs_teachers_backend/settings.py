"""
Django settings for acs_teachers_backend project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ
import os
import sys

# .env file
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file (AFTER INITIAL BASE_DIR)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Add /apps folder to python path 
# https://stackoverflow.com/a/3948821
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['example.com'])

"""
Project Apps Definitions
Django Apps - Django Internal Apps
Third Party Apps before django - Apps installed via requirements.txt, which add before django apps
Third Party Apps after django - Apps installed via requirements.txt, which add after django apps
Project Apps - Project owned / created apps
Installed Apps = Django Apps + Third Part apps + Projects Apps
"""

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS_BEFORE = [
    'grappelli',
]

THIRD_PARTY_APPS_AFTER = [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'drf_yasg',
    'dj_rest_auth'
]

PROJECT_APPS = [
    'journal',
    'teacher',
    'student',
    'lesson',
    'authorization',
]

INSTALLED_APPS = THIRD_PARTY_APPS_BEFORE + DJANGO_APPS + THIRD_PARTY_APPS_AFTER + PROJECT_APPS

# https://www.django-rest-framework.org/#example
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

"""
Middleware definitions
Django middleware - Django Internal middleware
Third Party middleware before django - Middleware installed via requirements.txt, which add before middleware
Third Party middleware after django - Middleware installed via requirements.txt, which add after middleware
"""

DJANGO_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',
]

THIRD_PARTY_MIDDLEWARE_BEFORE_DJANGO = [
    'corsheaders.middleware.CorsMiddleware',  # before ...CommonMiddleware
]

THIRD_PARTY_MIDDLEWARE_AFTER_DJANGO = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # after ...SecurityMiddleware
]

MIDDLEWARE = THIRD_PARTY_MIDDLEWARE_BEFORE_DJANGO + DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE_AFTER_DJANGO

ROOT_URLCONF = 'acs_teachers_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # os.path.join(BASE_DIR, 'templates')
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'acs_teachers_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL')
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

# https://docs.djangoproject.com/en/4.1/ref/settings/#locale-paths 
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True

# https://stackoverflow.com/a/70709867
USE_L10N = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Media files 

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin URL Definition
ADMIN_URL = env('ADMIN_URL', default='admin/')

# Logging configuration dictionary
# https://docs.djangoproject.com/en/4.1/ref/settings/#logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
        'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}


# CORS settings
# https://github.com/adamchainz/django-cors-headers#setup

if DEBUG:
    CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8080']
else:
    CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=['http://127.0.0.1:8080'])

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True


# DATE settings

DATE_INPUT_FORMATS = ['%d.%m.%Y']


# Auth settings

AUTH_USER_MODEL = 'authorization.User'


# REST authorization settings

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': env('JWT_AUTH_COOKIE'),
    'JWT_AUTH_REFRESH_COOKIE': env('JWT_AUTH_REFRESH_COOKIE'),
}
