from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    "django_ckeditor_5",
    'django_recaptcha',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'main.middleware.UnderConstMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samiportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processor.Site_Data'
            ],
        },
    },
]

WSGI_APPLICATION = 'samiportfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


#  static url settings
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": {
            "items": [
                'undo', 'redo',
                '|',
                'heading',
                '|',
                'fontFamily', 'fontSize', 'fontColor', 'fontBackgroundColor',
                '|',
                'bold', 'italic', 'strikethrough', 'subscript', 'superscript', 'code',
                '|',
                'link', 'uploadImage', 'blockQuote', 'codeBlock',
                '|',
                'alignment',
                '|',
                'bulletedList', 'numberedList', 'todoList', 'outdent', 'indent'
            ],
            "shouldNotGroupWhenFull": True
        },
        "placeholder": "Type your text here...",
        "link": {
            "defaultTarget": "_blank"
        },
        "height": 200,
        "fontColor": "#000000",
        "fontSize": {          # numeric font sizes
            "options": [
                "12px", "14px", "16px", "18px", "20px",
                "24px", "30px", "36px", "48px", "60px"
            ]
        }
    },
    "extends": {
        "toolbar": {
            "items": [
                'undo', 'redo',
                '|',
                'heading',
                '|',
                'fontFamily', 'fontSize', 'fontColor', 'fontBackgroundColor',
                '|',
                'bold', 'italic',
                '|',
                'link', 'uploadImage'
            ],
            "shouldNotGroupWhenFull": True
        },
        "placeholder": "Write project description here...",
        "height": 300,
        "fontSize": {
            "options": [
                "12px", "14px", "16px", "18px", "20px",
                "24px", "30px", "36px", "48px", "60px"
            ]
        }
    },
}

#  capchta setting

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')

UNDER_MAINTENANCE_KEY = config('UNDER_MAINTENANCE_KEY')

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# logging system............
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'detailed': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/errors.log'),
            'when': 'midnight',      # har din raat ko rotate karega
            'interval': 1,           # har 1 din
            'backupCount': 1,        # sirf 1 din purani file rakhega
            'formatter': 'detailed',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
