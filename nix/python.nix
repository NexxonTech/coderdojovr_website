{ pkgs }: let
  python = pkgs.python3;
in python.withPackages (ps: with ps; [
  django-extensions
  granian
  psycopg2
  pyopenssl
  requests
  wagtail
  werkzeug
  whitenoise
])
