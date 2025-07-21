from django.contrib.staticfiles.apps import StaticFilesConfig


class PortalStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = [ "*.src.*" ]
