from blog.settings.base import *
try:
    from blog.settings.local import *
except:
    pass

# Override base.py settings...

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += (
        # 'debug_toolbar',
    )

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
