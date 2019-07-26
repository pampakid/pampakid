from blog.settings.base import *
try:
    from blog.settings.local import *
except:
    pass

# Override base.py settings...

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          'OPTIONS': {
#              'sql_mode': 'traditional',
#          },
#          'NAME': 'db706p0v5ddsqa',
#          'USER': 'vcvjdsarxbqvxy',
#          'PASSWORD': 'c1f63deffce418824f0ad5a3923742b079c82a6f362ea7e6c1fa9b22086007ab',
#          'HOST': 'ec2-54-228-246-214.eu-west-1.compute.amazonaws.com',
#          'PORT': '5432',
#      }
#  }
