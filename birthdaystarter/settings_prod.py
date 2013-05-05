from settings_base import *

ENVIRONMENT = 'PROD'

ALLOWED_HOSTS = [
    'birthdaystarter.herokuapp.com',
    'giftly.ca',
    'www.giftly.ca',
]

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'birthdaystarter'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=%s' % (30 * 24 * 60 * 60),
}
COMPRESS_STORAGE = STATICFILES_STORAGE

STATIC_URL = 'https://s3.amazonaws.com/birthdaystarter/'
MEDIA_URL = 'https://s3.amazonaws.com/birthdaystarter/'

FACEBOOK_APP_ID = '363980993712828'
FACEBOOK_APP_SECRET = 'a93c979b7d23272a7bcc793bf9daec02'

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://ab1f113033a04d85985032a086338f25:0e5202a9000145d3b10cf7a8d7991a56@app.getsentry.com/8106',
}
