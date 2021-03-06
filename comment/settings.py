"""
Django settings for comment project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from alipay import Alipay

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q^%dxuzp7)-#o@(gk$eq=m4s_lenplol$cez)1hc(r6e1yn055'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'comment.urls'

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
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'comment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comment',
        'HOST': '192.168.1.97',
        'PORT': '3306',
        'USER': 'comment',
        'PASSWORD': 'comment',
        'OPTIONS': {'charset':'utf8'},
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
MEDIA_ROOT=os.path.join( BASE_DIR , 'media').replace('\\','/')
STATIC_ROOT=os.path.join( BASE_DIR , 'static').replace('\\','/')

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("imgs", os.path.join(STATIC_ROOT,'imgs')),
)

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE=1500

PID=''
KEY=''
SELLER_EMAIL=''
RETURN_URL='http://comment.xiuche580.com/pay_return'
NOTIFY_URL='http://comment.xiuche580.com/pay_notify'
ALIPAY=Alipay(pid=PID, key=KEY, seller_email=SELLER_EMAIL)


EMAIL_HOST='smtp.139.com'
EMAIL_PORT=25
EMAIL_HOST_USER=15002080574
EMAIL_HOST_PASSWORD=1988729
FROM_EMAIL='15002080574@139.com'



