import datetime
import os

AWS_WOW_USERS = {
    "wm-wm-public-user": {
        "k": os.environ['S3_KEY_WM_WM_PUBLIC_USER'],
        "s": os.environ['S3_SECRET_WM_WM_PUBLIC_USER'],
    },
    "wm-wm-user-user": {
        "k": os.environ['S3_KEY_WM_WM_USER_USER'],
        "s": os.environ['S3_SECRET_WM_WM_USER_USER'],
    },
    "wm-wm-members-user": {
        "k": os.environ['S3_KEY_WM_WM_MEMBERS_USER'],
        "s": os.environ['S3_SECRET_WM_WM_MEMBERS_USER'],
    }
}

AWS_ACCESS_KEY_ID = AWS_WOW_USERS["wm-wm-public-user"]["k"]
AWS_SECRET_ACCESS_KEY = AWS_WOW_USERS["wm-wm-public-user"]["s"]

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'wm.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'wm.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME'] # 'wm-wm-static-media'

# AWS_UPLOAD_USERNAME = "wm-Justin"
# AWS_UPLOAD_GROUP = "wm-dv-group"
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}