from .base import *


DEBUG = True
SECRET_KEY = "@(26l+ny$7g)1-3=en4c^3j9j=qph#pd*xl-a9xsl7ov7+5(a@"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "landregistry"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", 5432),
    }
}