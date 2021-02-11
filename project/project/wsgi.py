"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')

application = get_wsgi_application()

from django.conf import settings


if settings.DEBUG:
    try:
        import django.views.debug
        from werkzeug.debug import DebuggedApplication

        application = DebuggedApplication(
            application,
            evalex=True,
            # Turning off pin security as DEBUG is True
            pin_security=False,
        )
    except ImportError:
        pass
