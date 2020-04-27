# apodgram-django
## Deploy Steps
## Init
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```

### Procfile
```
web:  python manage.py runserver 0.0.0.0:$PORT --noreload
```
### settings.py
``` python
ALLOWED_HOSTS = ['apodgram-django-backend.herokuapp.com']


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # <=== This
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  

]

STATIC_URL = '/static/'

```


### CLI
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py collectstatic
heroku run python manage.py syncdb
```
