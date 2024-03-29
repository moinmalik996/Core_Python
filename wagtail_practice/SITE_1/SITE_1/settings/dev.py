from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@p7_w%gg@wqtqhkt3rc$6#e=vkwhekikf00eb-@25+5sh$vlpi'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
    'django_extensions',
    'menus',
    'contact'
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

CACHES = {
    'default': {
        'BACKEND' : 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:\\Users\\dev\\Desktop\\Moin\\Core_Python\\wagtail_practice\\SITE_1\\cache'
    }
}

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

try:
    from .local import *
except ImportError:
    pass
