from settings_base import *

ENVIRONMENT = 'DEV'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'birthdaystarter',
        'USER': 'birthdaystarter_admin',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

FACEBOOK_APP_ID = '144073369110744'
FACEBOOK_APP_SECRET = '1f2935bf3a19932d380649962e457578'
