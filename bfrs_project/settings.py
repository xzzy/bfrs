"""
Django settings for bfrs_project project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import dj_database_url
import ldap
import os
import sys

from confy import env, database, cache

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CRISPY_TEMPLATE_PACK = 'bootstrap3'

EMAIL_HOST = env('EMAIL_HOST', 'email.host')
EMAIL_PORT = env('EMAIL_PORT', 25)
FROM_EMAIL = env('FROM_EMAIL', 'from_email')
RDO_EMAIL = env('RDO_EMAIL', 'rdo_email')
PICA_EMAIL = env('PICA_EMAIL', 'pica_email')
PVS_EMAIL = env('PVS_EMAIL', 'pvs_email')
POLICE_EMAIL = env('POLICE_EMAIL', 'police_email')
DFES_EMAIL = env('DFES_EMAIL', 'dfes_email')
FSSDRS_EMAIL = env('FSSDRS_EMAIL', 'fssdrs_email')
EMAIL_TO_SMS_FROMADDRESS = env('EMAIL_TO_SMS_FROMADDRESS', 'pics_sms_from')
MEDIA_ALERT_SMS_TOADDRESS = env('MEDIA_ALERT_SMS_TOADDRESS', 'pica_sms_to')
ALLOW_EMAIL_NOTIFICATION = os.environ.get('ALLOW_EMAIL_NOTIFICATION', None) in ["True", "on", "1", "DEBUG"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
#SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.environ.get('DEBUG', None) in ["True", "on", "1", "DEBUG"]

ALLOWED_HOSTS = []

#DEBUG = os.environ.get('DEBUG', None) in ["True", "on", "1", "DEBUG"]
INTERNAL_IPS = ['127.0.0.1', '::1']
if not DEBUG:
    # Localhost, UAT and Production hosts
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        'bfrs.dpaw.wa.gov.au',
        'bfrs.dpaw.wa.gov.au.',
        'bfrs-uat.dpaw.wa.gov.au',
        'bfrs-uat.dpaw.wa.gov.au.',
        'bfrs-dev.dpaw.wa.gov.au',
        'bfrs-dev.dpaw.wa.gov.au.'
    ]

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'bfrs.dpaw.wa.gov.au',
    'bfrs.dpaw.wa.gov.au.',
    'bfrs-uat.dpaw.wa.gov.au',
    'bfrs-uat.dpaw.wa.gov.au.',
    'bfrs-dev.dpaw.wa.gov.au',
    'bfrs-dev.dpaw.wa.gov.au.'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'guardian',
    'tastypie',
    'smart_selects',
    'django_extensions',
    'debug_toolbar',
    'crispy_forms',
    'django_filters',

    'bfrs',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'dpaw_utils.middleware.SSOLoginMiddleware',
]

ROOT_URLCONF = 'bfrs_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'bfrs', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
#            'loaders': [
#                'django.template.loaders.cached.Loader',
#                'django.template.loaders.filesystem.Loader',
#                'django.template.loaders.app_directories.Loader',
#            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'bfrs_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {'default': database.config()}
#DATABASES = {'default': dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'guardian.backends.ObjectPermissionBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Australia/Perth'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
         'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'compressor.finders.CompressorFinder',

)

