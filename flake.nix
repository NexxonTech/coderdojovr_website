{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs { inherit system; };
        pkgs_armv7 = import nixpkgs {
          inherit system;
          crossSystem = { config = "armv7l-unknown-linux-gnueabihf"; };
        };
        pyenv = import ./nix/python.nix { inherit pkgs; };
        coderdojo_portal = import ./nix/coderdojo_portal.nix { inherit pkgs; };
      in {
        packages = {
          dockerimg = import ./nix/coderdojo_portal_docker.nix { inherit pkgs; inherit coderdojo_portal; };
          dockerimg_armv7 = import ./nix/coderdojo_portal_docker.nix { pkgs = pkgs_armv7; inherit coderdojo_portal; };
          pyenv = pyenv;
        };
        devShell = pkgs.mkShell {
          name = "coderdojo_website_dev";
          packages = with pkgs; [
            pyenv
            tailwindcss_4
          ];
        };
      }
    );
}
