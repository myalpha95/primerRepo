
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tb3r#i_x%i7e4h+j-a^e_6oien1uq*7@^rle#iq_p+20y46jj7'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
# Application definition

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cursos',
        'USER': 'postgres',
        'PASSWORD': 'fiNBAhb4anzDHdwC',
        'HOST': '35.193.67.194',
        'PORT': 5432,
    }
}
