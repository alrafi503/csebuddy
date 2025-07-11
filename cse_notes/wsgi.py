"""
WSGI config for cse_notes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cse_notes.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cse_notes.settings'
os.environ['DJANGO_SECRET_KEY'] = 'django-insecure-&epf9cf$96z1r!e)nbunfoxqll3&kzk0z2n(7mqt7874ujmtwq'
os.environ['DJANGO_DEBUG'] = 'False'

application = get_wsgi_application()
