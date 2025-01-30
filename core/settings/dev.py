from .base import *

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAILADMIN_BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
