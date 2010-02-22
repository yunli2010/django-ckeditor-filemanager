# Django settings for project.
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendor'))
PROJECT_DIR = os.path.dirname(__file__)

# These settings can be over-ridden in settings_local.py
# -----------------------------------------------------------------------------------------

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_DOMAIN = "newproject.co.za"
PROJECT_NAME = "newproject"

ADMINS = (
    ('Paul von Hoesslin', 'paulvonhoesslin@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'newproject.sql'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# Email settings
EMAIL_TEST_MODE = True
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_SYSTEM_SENDER = 'newproject <noreply@newproject.co.za>'

TIME_ZONE = 'Africa/Johannesburg'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'static/')
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/media/'


#ATTENTION - Please configure

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd)bduv1z@xo#(xi*+cr&my-h-cws36bs8qqd#1@8q$niv7gh**'

FLICKR_API_KEY = ''
FLICKR_USER_ID = '-@-'

FCKEDITOR_CONNECTOR_PREFIX = ('/Users/jv/development/django/%s/static/') % PROJECT_NAME
FCKEDITOR_CONNECTOR_URL = '/static/'

GOOGLE_MAPS_API_KEY = {
    "localhost": "ABQIAAAAWvB8IvoFKDEO-Hpp2pbMoRRi_j0U6kJrkFvY4-OX2XYmEAa76BTYVM51Sh2Lk7Zr6TxPTksPXBVm6A",
    "online": "GO GET A KEY HERE: http://code.google.com/apis/maps/signup.html",
}
GOOGLE_API_STATUS = "online"

#-----------------------------------------


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'newproject.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'common',
    'vendor.flickrapi',
    'vendor.filemanager',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "common.context_processors.commonModels",
)

TEST_EMAIL_DIR = os.path.join(os.path.dirname(__file__), 'tmp', 'test_emails')

try:
    from settings_local import *
    print "Loaded settings_local.py"
except ImportError:
    print "Couldn't find settings_local.py, no settings overridden."
