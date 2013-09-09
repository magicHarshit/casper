import os.path
import os.path


PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER = 'harshit.py@gmail.com'
EMAIL_HOST_PASSWORD = 9015598983
EMAIL_PORT='587'
EMAIL_USE_TLS=True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

TIME_ZONE = 'America/Chicago'

SITE_ID = 1

USE_I18N = True
LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    )
LANGUAGE_CODE = 'en'
MODEL_I18N_CONF = 'i18n_conf'
MODEL_I18N_MASTER_LANGUAGE = LANGUAGE_CODE


#url to project static files
STATIC_ROOT = '/home/harshit/workspace/code/casper2/wsgi/openshift/'
STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'master.middleware.AuthenticationMiddleware'
    )

ROOT_URLCONF = os.path.basename(os.path.dirname(__file__)) + '.urls'


#UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = os.path.join(
    os.path.dirname(__file__),
    'tmp'
).replace('\\','/')

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
    )

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'master',
    )

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

STATICFILES_DIRS = (
    '/home/harshit/workspace/code/casper2/wsgi/openshift/static/',
    )
#delayed notifications, time in seconds, 15 mins by default
NOTIFICATION_DELAY_TIME = 60 * 15

SECRET_KEY = 'o3e(t&1l8(1j_!gn@m+r=km28&!zdazm2m)6n@eze6h=f$nq2#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mo',  # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

## List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)
MEDIA_ROOT = '/home/harshit/workspace/code/casper2/wsgi/openshift/media/'
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'master.MyUser'
