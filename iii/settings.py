"""
Django settings for iii project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if (
    DEBUG
):  # localhost and "diverse-intense-" must be in list for password reset functionality
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "diverse-intense-whippet.ngrok-free.app"]
    # ALLOWED_HOSTS = ["diverse-intense-whippet.ngrok-free.app", "localhost:8000"]
else:
    ALLOWED_HOSTS = ["vercel-3-5-2024.vercel.app"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Homepage",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # comment it if X-FRAME OPTION is None
]

ROOT_URLCONF = "iii.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]
WSGI_APPLICATION = "iii.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URLS = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Define the directory where media files will be uploaded and stored
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# AUTH_USER_MODEL = "Homepage.CustomUser"
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login/"
# CRISPY_TEMPLATE_PACK = "bootstrap5"
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


###########################Security Related Settings########################################

# Uncomment these settings only in production
if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_SSL_REDIRECT = True


# Google api-client library settings
# GOOGLE_OAUTH_CLIENT_ID = config("GOOGLE_OAUTH_CLIENT_ID")
# GOOGLE_OAUTH_CLIENT_SECRET = config("GOOGLE_OAUTH_CLIENT_SECRET")
# if not DEBUG:
#     GOOGLE_OAUTH_REDIRECT_URI = [
#         "https://osama11111.pythonanywhere.com/accounts/google/login/callback/"]
# else:
#     GOOGLE_OAUTH_REDIRECT_URI = ["http://localhost:8000/accounts/google/login/callback/"]
#         # "https://diverse-intense-whippet.ngrok-free.app/accounts/google/login/callback/"]


# csrf settings
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True
if DEBUG:
    CSRF_TRUSTED_ORIGINS = ["https://diverse-intense-whippet.ngrok-free.app"]
else:
    CSRF_TRUSTED_ORIGINS = ["https://vercel-3-5-2024.vercel.app"]
