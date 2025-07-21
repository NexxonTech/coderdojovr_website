{ pkgs, coderdojo_portal }: let
  pyenv = import ./python.nix { inherit pkgs; };
in pkgs.dockerTools.buildLayeredImage {
  name = "coderdojo_portal";
  tag = "0.1.0";
  created = "now";

  contents = [
    coderdojo_portal
    pyenv
  ] ++ (with pkgs.dockerTools; [
    binSh
    fakeNss
  ]);

  config = {
    Cmd = [ "/bin/sh" "/lib/coderdojo_portal/ContainerRunner.sh" ];
    Env = [
      "CODERDOJO_PORTAL_CONFIG=/etc/coderdojo_portal/Settings.toml"
      "CODERDOJO_PORTAL_STORAGE=/var/coderdojo_portal/"
    ];
    Volumes = {
      "/etc/coderdojo_portal" = {};
      "/var/coderdojo_portal" = {};
    };
  };
}
