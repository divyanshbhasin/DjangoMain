from .base import *


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]
INTERNAL_IPS = ['127.0.0.1', 'localhost']

MIDDLEWARE +=[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

