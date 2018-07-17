try:
	from project.settings.base import *
	from project.settings.secrets import *
except ImportError:
    pass

DEBUG = False


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_STORAGE_BUCKET_NAME = 'jsorg-docker-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#For hosting static files on S3. Causes TinyMCE popups to break.
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 's3_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATIC_ROOT = "/static/" 

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 's3_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = "media/" 


# DB Backup 
DBBACKUP_STORAGE = 'dbbackup.storage.s3_storage'
DBBACKUP_S3_BUCKET = 'dbbackup'