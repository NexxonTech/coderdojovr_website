import os
from django.http import FileResponse
from django.utils._os import safe_join
from django.core.exceptions import SuspiciousFileOperation
from django.conf import settings

class MediaMiddleware:
    def __init__(self, app):
        self.app = app
        self.media_root = settings.MEDIA_ROOT
        self.media_url = settings.MEDIA_URL

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")
        if path.startswith(self.media_url):
            rel_path = path[len(self.media_url):]
            try:
                file_path = safe_join(self.media_root, rel_path)
                if os.path.exists(file_path):
                    return FileResponse(open(file_path, "rb"))
            except (SuspiciousFileOperation, ValueError):
                pass
        return self.app(environ, start_response)
