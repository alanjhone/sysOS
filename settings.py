"""
Django settings for sysOS project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i+4@#!rg!t2i20rv466#a)-(ybxhi6qy#+#g&d5rl-_*02*z&b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'localflavor',
    'rest_framework',
    'sysOS.API',
    'sysOS.core',
    'sysOS.workshop',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE_CLASSES = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

ROOT_URLCONF = 'sysOS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sysOS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sysOS',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


INTERNAL_IPS = ('127.0.0.1',)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = 'core:login'
LOGIN_REDIRECT_URL = 'core:home'


# DEBUG-TOOLBAR
DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    # 'debug_toolbar.panels.timer.TimerPanel',
    # 'debug_toolbar.panels.settings.SettingsPanel',
    # 'debug_toolbar.panels.headers.HeadersPanel',
    # 'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]

# Django DebugToolbar Config
SHOW_DEBUG_TOOLBAR = DEBUG

def show_debug_toolbar(request):
    return SHOW_DEBUG_TOOLBAR

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_debug_toolbar,
    'INTERCEPT_REDIRECTS': False
}