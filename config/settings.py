from pathlib import Path
import os 
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-zb7f#qv)08s-!02uel&kjb=n0%6981s_h!y4zza+9g(ai3_$&z'
DEBUG = True
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "jazzmin",
    "modeltranslation",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.flatpages",
    "debug_toolbar",
    'drf_spectacular',
    "rest_framework",
    'ckeditor',
    'ckeditor_uploader',
    'apps.main',
    'apps.page_generator',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

SITE_ID = 1  

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
    ("ky", _("Кыргызча")),
)

STATIC_URL = "/back-static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back-static")

MEDIA_URL = '/back-media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "back-media")


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule']},
        ],
        'height': 200,
        'width': '140%',
        'extraPlugins': 'autogrow',
        'autoGrow_minHeight': 200,
        'autoGrow_maxHeight': 600,
        'autoGrow_bottomSpace': 50,
        'removePlugins': 'elementspath',
        'allowedContent': True,
        'extraAllowedContent': 'img[alt,border,width,height,align];a[!href];',
        'language': 'ru',
        'uiColor': '#9AB8F3',
    },
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'KAI API',
    'DESCRIPTION': 'KAI description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     },
#     'redis_cache': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://redis:6379/0', 
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

JAZZMIN_SETTINGS = {
    "site_header": "KAI",
    "site_brand": "KAI",
    "welcome_sign": "Welcome to the library",
    "search_model": ["auth.User"],

    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        {"model": "auth.User"},
        
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailINFO': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
            'formatter': 'detailINFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}