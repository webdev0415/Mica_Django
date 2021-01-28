from mica_django.base_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'az+wv*ipy@gjfo=jpxn1dz&c@^9x-n-9m&yb579trh(7*im_!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2k0b436k14etr',
        'USER': 'ojllqbwycqqwoy',
        'PASSWORD': 'f21738c5889c44875f1afaf9ee3ffcb4ad705907af677041c4bddd8e91d3e3bb',
        'HOST': 'ec2-75-101-232-85.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]