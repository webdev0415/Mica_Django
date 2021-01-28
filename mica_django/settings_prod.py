import os
import dj_database_url


from mica_django.base_settings import *

ALLOWED_HOSTS = ['*']


DEBUG = get_env_variable("DEBUG", "False") == "True"

SECRET_KEY = get_env_variable("SECRET_KEY")

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(
    get_env_variable('DATABASE_URL'), conn_max_age=600)

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# STATIC_URL = '/static/'

# STATICFILES_DIR = (
#     os.path.join(BASE_DIR, 'staticfiles'),
# )

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')