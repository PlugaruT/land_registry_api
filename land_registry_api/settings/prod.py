import os

import dj_database_url

from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

ENVIRONMENT = "prod"
DEBUG = False
ALLOWED_HOSTS = ["*"]
DATABASES["default"] = dj_database_url.config(
    default=os.environ.get("DATABASE_URL", None)
)
