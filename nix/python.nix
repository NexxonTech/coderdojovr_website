{ pkgs }: let
  pypkgs = pkgs.callPackage ./python-packages.nix { };
  python = pkgs.python3.override { packageOverrides = pypkgs; };
in python.withPackages (ps: with ps; [ appwrite flask granian ])