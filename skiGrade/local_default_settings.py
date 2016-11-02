import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = not DEBUG
COMPRESS_ENABLED = not DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #, 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ikea-production',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
    }
}

RAVEN_CONFIG = {}
