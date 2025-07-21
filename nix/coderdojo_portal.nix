{ pkgs }: let
  pyenv = import ./python.nix { inherit pkgs; };
in pkgs.stdenvNoCC.mkDerivation {
  pname = "coderdojo_portal";
  version = "0.1.0";
  src = ./..;

  buildPhase = ''
    ${pkgs.tailwindcss_4}/bin/tailwindcss -m -i portal/static/css/main.src.css -o portal/static/css/main.min.css
    DJANGO_SETTINGS_MODULE=coderdojo_portal.settings.base ${pyenv}/bin/python manage.py collectstatic
  '';

  installPhase = ''
    mkdir -p $out/lib/coderdojo_portal/
    cp -r coderdojo_portal/ search/ portal/ static/ config.py manage.py ContainerRunner.sh $out/lib/coderdojo_portal/
  '';
}
