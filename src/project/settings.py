from os import getenv
from pathlib import Path

import allauth
import crispy_forms
import dj_database_url
import grappelli
# import captcha

from allauth import account
from django.urls import reverse_lazy
from dynaconf import settings as _settings

# import telebot


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()

SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS

# bot = telebot.TeleBot(_settings.BOT_TOKEN)
#
# TELEGA_ADMIN = _settings.TELEGA_ADMIN


# Application definition

INSTALLED_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "captcha",
    "apps.subscription",
    "rest_framework",
    "apps.index",
    "apps.cv",
    "apps.projects",
    "apps.blog.apps.BlogConfig",
    "apps.myauth",
    "apps.api",
    "allauth",
    "allauth.account",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

RECAPTCHA_PUBLIC_KEY = _settings.RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = _settings.RECAPTCHA_PRIVATE_KEY
RECAPTCHA_DEFAULT_ACTION = "generic"
RECAPTCHA_SCORE_THERSHOLD = 0.5

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

# Database

DATABASE_URL = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    DATABASE_URL = getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600),
}
#     {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': (BASE_DIR / 'db.sqlite3').as_posix(),
# }


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/assets/"

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = REPO_DIR / ".static"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Sentry
if not DEBUG:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=_settings.SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
    )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



# @bot.message_handler()
# if username is not None:
#     Client_ip = request.META['REMOTE_ADDR']
#     bot.send_message(TELEGA_ADMIN.chatid, Client_ip + 'авторизовался на AY2YA', bot.get_me().username)

# LOGIN_URL = reverse_lazy("templates:sign_in")
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SITE_ID = 1
