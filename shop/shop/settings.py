from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4vazklifj^uzh_v^eitv3i7%ij&7h^wi!r52bfi_r_xez0uf9m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'products:home'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
    # third-party apps
    # pip install django-storages; see more on https://django-storages.readthedocs.io/en/latest/
    'storages', 
    # pip install django-celery-beat; see more on https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
    'django_celery_beat',# use python manage.py migrate to create table for celery beat
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

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'orders.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# pip install pip install psycopg2-binary
# sudo apt-get install postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mockingbird',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# sudo snap install redis
# pip install redis
# pip install hiredis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'accounts.User'
# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# For static files that don't belong to a specific app
STATICFILE_DIRS = [
    BASE_DIR / 'static'
]

# media files
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#############################################################################
# Google smtp 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'amirafshar.d@gmail.com'
EMAIL_HOST_PASSWORD = 'ddejrfqsloyuhifk'

#############################################################################

# arvancloud
# more on https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '5a987142-a0f5-4d10-8629-874ae892a2cb'
AWS_SECRET_ACCESS_KEY = 'a591ad1cdffba06e8172a8485044d18b0ad1e5505134ed263de7037ea2f12e45'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_STORAGE_BUCKET_NAME = 'dj-shop'
AWS_S3_FILE_OVERWRITE = False
AWS_SERVICE_NAME = 's3'
AWS_LOCAL_STORAGE = BASE_DIR / '/aws/'
