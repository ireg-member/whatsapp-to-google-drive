"""
Django settings for whatsapp_drive project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6g_z$s@g(6ngs(arq_!4w644=8=^rg!(#+ex*a6zo3x0!f)6f%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'whatsapp_drive.urls'

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

WSGI_APPLICATION = 'whatsapp_drive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Twilio account
TWILIO_ACCOUNT_SID = 'AC866e45b7e3938e0cfd678fdc755bb461'
AUTH_TOKEN = '277e5c86104afef9af37c8e9fcdce61d'
GOOGLE_CLIENT_ID = "77197195058-3srhnpl1a55lshnb8fr2uhbdc8fbodkn.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_ACCESS_TOKEN = 'ya29.a0Ad52N3_2MOtlf5GDgDt72AyXG3xJ-scB3tX1lus-QUhpwNHpUsxL9bYcf9_MGrzwQmOiC1tyBhjpqFY0m7eoSp-g9CaEER5-_9uv5fTPOXOjQ2xe9npZQrEa6DRk7h1PTIUC2CfFX8CHEB7l1JkxwR3wG_MW0ayuWY7BaCgYKAUkSARASFQHGX2MiKbawWXEynBvAmoI7718iBg0171'
GOOGLE_REFRESH_TOKEN = '1//04V_t12HPB1XYCgYIARAAGAQSNwF-L9IrMhn-hf7fwcIHEXxo408jzCPtXAtLl15Q8_P2nbNgbmhf2ZTUKL63_dDGe2FWweTTUk4'
