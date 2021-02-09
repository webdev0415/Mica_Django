from mica_django.base_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'az+wv*ipy@gjfo=jpxn1dz&c@^9x-n-9m&yb579trh(7*im_!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd2k0b436k14etr',
#         'USER': 'ojllqbwycqqwoy',
#         'PASSWORD': 'f21738c5889c44875f1afaf9ee3ffcb4ad705907af677041c4bddd8e91d3e3bb',
#         'HOST': 'ec2-75-101-232-85.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd9v89qak4p5fl8',
#         'USER': 'rkjgpgunvofpws',
#         'PASSWORD': '03cb1ce45185cb70077acf3b73fc0b4bae1f17937b0058ce9fa62254472570ac',
#         'HOST': 'ec2-50-16-108-254.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'advi',
        'USER': 'postgres',
        'PASSWORD': 'BillGates94415',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'oe2',
#         'USER': 'root',
#         'PASSWORD': 'aQfeW4D3',
#         'HOST': 'st-writer-rds.advinow-dev.int',
#         'PORT': '5432',
#     }
# }

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