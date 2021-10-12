"""
Django settings for django_test_r project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# folder which is holding manage.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#It is unique to the project
SECRET_KEY = '&l7tfnvgy3*wma)4gabzh$jhbmi^7q!h(7w2%p$qos^@(s78x5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Domain names which are allowed
ALLOWED_HOSTS = []


# Application definition
# Build your apps here, products, think of it as components, little djago project itself
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # put you own apps and third party apps here
    'articles',
]

# How request and securities are handled
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# this is how django knows how to route and get a url
ROOT_URLCONF = 'django_test_r.urls'

#how we store them, how they are rendered and how they work
#It's basically html page which is rendered in django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# this is how server works
WSGI_APPLICATION = 'django_test_r.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#django maps to this databases, you can change the backend here, where it is located and some other settings
#by default it has sqlite3 database already there
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# where do you store your static files, images, java script, css
STATIC_URL = '/static/'

#you can add media here like images using media
# MEDIA_URL = '/__/'
# MEDIA_ROOT = os.path.join(BASE_DIR, '')
