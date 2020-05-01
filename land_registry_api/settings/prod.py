from .base import *
import dj_database_url

# SECRET_KEY = os.environ.get("SECRET_KEY")

ENVIRONMENT = 'prod'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='postgres://cnzgrcninaokmr:a8c1d78511f743b041fe30a7c4702903cb40a7df3c62bfe8406fec1a3c7e86db@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d9jaiqletq5gf3'
)