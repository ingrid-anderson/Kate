import datetime
import os

AWS_ACCESS_KEY_ID = "AKIAIZGDP6ARV5OO4N7A"  # "AKIAI4ELCXQMLV6QIE2A"
AWS_SECRET_ACCESS_KEY = "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"  # "HVignQ85OVOZx6SNgGLWfZfc4VHeDsSix9UVvwgY"
#user name is django-user

PREPEND_WWW = True

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'wm.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'wm.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME =  'ka-bucket' # 'wm-dv-static-media'
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