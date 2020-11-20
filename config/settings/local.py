"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH'
)
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "18.222.126.99",
]

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
