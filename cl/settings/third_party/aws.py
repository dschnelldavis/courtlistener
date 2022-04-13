import environ

env = environ.FileAwareEnv()
DEVELOPMENT = env.bool("DEVELOPMENT", default=True)

if DEVELOPMENT:
    AWS_ACCESS_KEY_ID = env("AWS_DEV_ACCESS_KEY_ID", default="")
    AWS_SECRET_ACCESS_KEY = env("AWS_DEV_SECRET_ACCESS_KEY", default="")
else:
    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")

AWS_STORAGE_BUCKET_NAME = env(
    "AWS_STORAGE_BUCKET_NAME", default="com-courtlistener-storage"
)
AWS_S3_CUSTOM_DOMAIN = "storage.courtlistener.com"
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False

if DEVELOPMENT:
    AWS_STORAGE_BUCKET_NAME = "dev-com-courtlistener-storage"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

CLOUDFRONT_DOMAIN = env("CLOUDFRONT_DOMAIN", default="")

AWS_LAMBDA_PROXY_URL = env("AWS_LAMBDA_PROXY_URL", default="")