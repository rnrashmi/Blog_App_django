"""
WSGI config for MyBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjagoWhiteNoise

path = "/home/"

if path not in sys.path:
  sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyBlog.deploy_settings')

application = get_wsgi_application()
application = DjagoWhiteNoise()
