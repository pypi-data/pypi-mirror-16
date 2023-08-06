"""
Django settings for our wheresyourtrash project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

from configurations import Configuration, values
from celery.schedules import crontab


class Common(Configuration):

    ADMINS = (
        ('Admin', 'info@example.com'),
    )

    # You'll likely want to add your own auth model.
    AUTH_USER_MODEL = 'custom_user.EmailUser'

    MANAGERS = ADMINS

    SECRET_KEY = 'notasecretatall'

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, 'wheresyourtrash/apps'))

    USE_SOUTH = False

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    # Application definition

    INSTALLED_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        'whitenoise.runserver_nostatic',
        "django.contrib.staticfiles",

        'custom_user',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.google',
        "django_extensions",
        'floppyforms',
        'rest_framework',
        'crispy_forms',
        'materializecssform',


        # Custom apps
        'notifications',
        'email2sms',

    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, "wheresyourtrash/templates") ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                    # list if you haven't customized them:
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.core.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    )

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USERNAME_REQUIRED = False

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",)

    ROOT_URLCONF = 'wheresyourtrash.urls'

    WSGI_APPLICATION = 'wheresyourtrash.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3'),
        environ=True))

    BROKER_URL = values.Value('redis://localhost:6379/0')
    BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    CELERYBEAT_SCHEDULE = {
        'send_notifications_at_6am': {
            'task': 'notifications.tasks.send_notifications',
            'schedule': crontab(minute=0, hour=6),
        },
    }

    NEVERCACHE_KEY = values.Value('klladsf-wefkjlwef-wekjlwef--wefjlkjfslkxvl')

    #CACHES = values.CacheURLValue('memcached://127.0.0.1:11211')

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('America/New_York')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

    PUBLIC_ROOT = values.Value(os.path.join(BASE_DIR, 'public'))
    STATIC_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "wheresyourtrash/static"),
    )

    MEDIA_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'media')
    MEDIA_URL = "/media/"

    #AWS_ACCESS_KEY_ID = values.Value()
    #AWS_SECRET_ACCESS_KEY = values.Value()
    #AWS_STORAGE_BUCKET_NAME = 'wheresyourtrash.com'
    #AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
    #               'Cache-Control': 'max-age=86400', }
    #
    #AWS_ENABLED = values.BooleanValue(False)

    #if AWS_ENABLED:
    #    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 14

    LOGIN_EXEMPT_URLS = ['', '/',
                         '/accounts/login/',
                         'login',
                         '/accounts/signup/']

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_URL = '/accounts/logout/'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }



class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(Common.BASE_DIR, 'db.sqlite3'),
        environ=True))

    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = values.Value('localhost')
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value('1025')
    EMAIL_USE_TLS = values.BooleanValue(False)


    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)


class Stage(Common):
    DEBUG = True

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value('localhost')
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(False)


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = False

    SECRET_KEY = values.SecretValue()
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(True)

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    RAVEN_CONFIG = {
        'dsn': DSN_VALUE.setup('DSN_VALUE'),
    }

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)
