"""
WSGI config for python2sites project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling

path = '/home/django/python2sites'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python2sites.settings")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
