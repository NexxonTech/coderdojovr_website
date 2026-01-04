{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, flake-utils, nixpkgs, ... }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs { inherit system; };
        daisyui = pkgs.fetchurl {
          url = "https://github.com/saadeghi/daisyui/releases/download/v5.5.14/daisyui.mjs";
          sha256 = "sha256-ZhCaZQYZiADXoO3UwaAqv3cxiYu87LEiZuonefopRUw=";
        };
        coderdojo_portal = pkgs.stdenvNoCC.mkDerivation {
          pname = "coderdojo_portal";
          version = "0.1.0";

          src = ./.;

          buildPhase = ''
            cp ${daisyui} static/assets/styles/daisyui.mjs
            ${pkgs.tailwindcss_4}/bin/tailwindcss -m -i static/assets/styles/main.src.css -o static/assets/styles/main.min.css
            ${pkgs.zola}/bin/zola build
          '';

          installPhase = ''
            cp -r public/ $out/
          '';
        };
      in {
        defaultPackage = coderdojo_portal;
        devShell = pkgs.mkShell {
          name = "coderdojo_portal_devenv";
          packages = (with pkgs; [
            ferron
            tailwindcss_4
            zola
          ]);
        };
      }
    );
}
