from common import *

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['admin.niteabout.com', 'niteabout.com']


STATICFILES_STORAGE = 'niteabout.storage.MyBoto'
DEFAULT_FILE_STORAGE = 'niteabout.storage.MyBoto'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_QUERYSTRING_AUTH = False


S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

STATIC_ROOT = "static/"
MEDIA_ROOT = "media/"

STATIC_URL = S3_URL + STATIC_ROOT
MEDIA_URL = S3_URL + MEDIA_ROOT

INSTALLED_APPS += ('gunicorn', 'storages','pyqs',)

EMAIL_USE_TLS = True
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.eniron['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
