"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from backend.settings import DEBUG
from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.production")

application = get_wsgi_application()
app = application
