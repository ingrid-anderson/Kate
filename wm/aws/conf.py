import datetime
import os

AWS_USERS = {
    "django-user": {
        "k": os.environ['S3_KEY_KA_PUBLIC_USER'],
        "s": os.environ['S3_SECRET_KA_PUBLIC_USER'],
    },
}

AWS_ACCESS_KEY_ID = AWS_USERS["django-user"]["k"]
AWS_SECRET_ACCESS_KEY = AWS_USERS["django-user"]["s"]

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
PREPEND_WWW = True

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'wm.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'wm.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME =  os.environ['AWS_STORAGE_BUCKET_NAME'] # 'wm-dv-static-media'
# AWS_UPLOAD_USERNAME = "wm-Justin"
# AWS_UPLOAD_GROUP = "wm-dv-group"
S3DIRECT_REGION = 's3-us-west-2'
S3_URL = '//%s.amazonaws.com/%s/' % (S3DIRECT_REGION, AWS_STORAGE_BUCKET_NAME)
# MEDIA_URL = '//%s.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

# PROTECTED_DIR_NAME = 'media'
# PROTECTED_MEDIA_URL_SSS = '//%s.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, PROTECTED_DIR_NAME)
# PROTECTED_MEDIA_URL = '//%s.%s.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, S3DIRECT_REGION, PROTECTED_DIR_NAME)

# MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

one_day = datetime.timedelta(days=1)
date_day_later = datetime.date.today() + one_day
expires = date_day_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(one_day.total_seconds()),),
}