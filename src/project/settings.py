

import dj_database_url

from os import getenv
from pathlib import Path
from dynaconf import settings as _settings
from django.urls import reverse_lazy



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _settings.SECRET_KEY
    # '%jb(pw*+h=g25+bwhn7$))d8(464k7lpansid%=92mf-v_qegq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _settings.DEBUG
        # True

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS
#     [
#     "127.0.0.1",
#     "localhost",
#     "yyyakovlev.herokuapp.com",
# ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.index',
    'apps.cv',
    'apps.projects',
    'apps.blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'


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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Sentry
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

STATIC_URL = '/assets/'

STATICFILES_DIRS = [
    PROJECT_DIR / 'static',
]

STATIC_ROOT = REPO_DIR / ".static"

LOGIN_URL = reverse_lazy("onboarding blabla") # перенаправление юзера если он зашел туда куда нельзя
LOGIN_REDIRECT_URL = reverse_lazy("blog:all_post") # перенаправление юзера после логина