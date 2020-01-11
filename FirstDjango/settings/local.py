from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'li-uwil7d3j@*!994c+#(*5a6j3ske)&7374rc&ne)@(!igh9$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

############

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbtest',
        'USER': 'root',
        'PASSWORD': 'mysql@123.com',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
