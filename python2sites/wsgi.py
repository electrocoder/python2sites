"""
WSGI config for python2sites project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home')
sys.path.append('/home/django')
sys.path.append('/home/django/python2sites')
sys.path.append('/home/django/python2sites/python2sites')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python2sites.settings")

application = get_wsgi_application()
