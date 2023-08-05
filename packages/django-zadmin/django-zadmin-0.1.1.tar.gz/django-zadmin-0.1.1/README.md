# django-zadmin
another admin template for django with bootstrap4.0 and sass


## **It is not unavailable now** ##


### Install ###

use `pip` to install `django-zadmin`.

> pip install django-zadmin


### How to use django-zadmin?###

1. Anytime, open `settings.py`, and add app `zadmin` to `INSTALLED_APPS`

  ```python
  INSTALLED_APPS = [
      # keep 'django.contrib.admin' here.
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'zadmin',
      # other app
  ]
  ```

2. Set `STATIC_ROOT` and `TEMPLATES` in `settings.py`

  ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    ...

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                # Here
                os.path.join(BASE_DIR, 'templates')
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

  ```

3. Run `python manage.py copy_templates_and_static` to copy admin's template files and static files

  >python manage.py copy_templates_and_static

4. That's OK

  >python manage.py runserver


### try example ###

When you have this repository downloaded, you can play with example immediately.

1. Open `example` directory.
2. export environment variable named as `PYTHONPATH`

  > export PYTHONPATH=/**repo_path**/zadmin

  please replace **repo_path** to your repository path.
3. run `python manage.py runserver`
