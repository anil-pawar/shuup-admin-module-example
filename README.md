This is Sample SHUUP model

Add 'example.first' in INSTALLED_APPS in your settings.py

e.g.

INSTALLED_APPS = [
    'example.first'
]

Run migrate to update/update DB setup scripts:

python manage.py migrate