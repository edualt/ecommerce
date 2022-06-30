from pathlib import Path
import environ
import os
from datetime import timedelta

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')

# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users',
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    # 'DEFAULT_PERMISSION_CLASSES' : [
    #         'rest_framework.permissions.AllowAny',
    #     ],
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        ],
    'DEFAULT_PARSER_CLASSES' : [
            'rest_framework.parsers.JSONParser',
        ]
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

AUTH_USER_MODEL = 'users.User'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

