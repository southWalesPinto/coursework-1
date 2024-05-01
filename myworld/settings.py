import os
from pathlib import Path
from easy_thumbnails.conf import Settings as thumbnail_settings

# Set the secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-a5w#s8w02_887j5(#_0bym8d+&s18ctd&o@-%(kl*kp)b329*d')

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug mode
DEBUG = True 



# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Custom user model
AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account.apps.AccountConfig',
    'Booking.apps.BookingConfig',
    'Cart.apps.CartConfig',
    'oauth2_provider',
    'easy_thumbnails',
    'image_cropping',
]
THUMBNAIL_PROCESSING = (
    'image_cropping.thumbnail_processors.crop_corneres',    
 ) +  thumbnail_settings.THUMBNAIL_PROCESSORS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.ApprovalMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Custom middleware added here
]

# Root URL configuration
ROOT_URLCONF = 'myworld.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates'),  # Main templates directory
             os.path.join(BASE_DIR, 'Booking', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Cart.context_processors.cart',
            ],
        },
    },
]
EMAIL_CONFIRMATION_REQUIRED = True

# WSGI application
WSGI_APPLICATION = 'myworld.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators
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

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration
# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]
STATIC_ROOT = str(BASE_DIR / 'productionfiles')


# Custom authentication backends
AUTHENTICATION_BACKENDS = [
    'account.backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# OAuth2 Provider Settings
OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups',
    }
}


# Media root directory where uploaded files will be stored
MEDIA_ROOT = BASE_DIR / 'media'

# Media URL to serve uploaded files
MEDIA_URL = '/media/'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server address
EMAIL_PORT = 587  # SMTP server port
EMAIL_USE_TLS = True  # Whether to use TLS (secure connection) for sending emails
EMAIL_HOST_USER = 'hads1kiki@gmail.com'  # SMTP username (your email address)
EMAIL_HOST_PASSWORD = 'jxrt rxfv xrrh fono'  # SMTP password for authentication
EMAIL_SUBJECT_PREFIX = '[MyApp] '  # Email subject prefix (optional)
ADMIN_EMAIL = 'hads1kiki@gmail.com'  # Admin email address (optional)
DEFAULT_FROM_EMAIL = 'hads1kiki@gmail.com'  # Default sender email address (optional)

# IMAGE CROPPING Configuration
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}