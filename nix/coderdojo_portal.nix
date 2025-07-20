{ pkgs }: pkgs.stdenvNoCC.mkDerivation {
  pname = "coderdojo_portal";
  version = "0.1.0";
  src = ./..;

  buildPhase = ''
    ${pkgs.tailwindcss_4}/bin/tailwindcss -m -i static/assets/styles/main.src.css -o static/assets/styles/main.min.css
  '';

  installPhase = ''
    mkdir -p $out/lib/coderdojo_portal/
    cp -r src/ static/ template/ $out/lib/coderdojo_portal/
  '';
}