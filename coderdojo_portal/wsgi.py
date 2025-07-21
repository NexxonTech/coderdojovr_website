"""
WSGI config for coderdojo_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from coderdojo_portal.media_middleware import MediaMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coderdojo_portal.settings.production")

application = MediaMiddleware(get_wsgi_application())
