{ pkgs }: let
  pypkgs = pkgs.callPackage ./python-packages.nix { };
  #python = pkgs.python3.override { packageOverrides = pypkgs; };
  python = pkgs.python3;
in python.withPackages (ps: with ps; [
  #appwrite
  #flask
  #flask-login
  granian
  psycopg2
  wagtail
  whitenoise
])
