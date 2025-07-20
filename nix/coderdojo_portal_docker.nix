{ pkgs, coderdojo_portal }: let
  pyenv = import ./python.nix { inherit pkgs; };
in pkgs.dockerTools.buildLayeredImage {
  name = "coderdojo_portal";
  tag = "0.1.0";
  created = "now";

  fromImage = pkgs.dockerTools.pullImage {
    imageName = "alpine";
    imageDigest = "sha256:4bcff63911fcb4448bd4fdacec207030997caf25e9bea4045fa6c8c44de311d1";
    finalImageTag = "3.22.1";
    sha256 = "sha256-oBoU1GqTLZGH8N3TJKoQCjmpkefCzhHFU3DU5etu7zc=";
  };

  contents = [ coderdojo_portal pyenv ];

  config = {
    Cmd = [ "python" "-m" "granian" "--interface" "wsgi" "--host" "0.0.0.0" "/lib/coderdojo_portal/src:app"];
    Env = [ "CODERDOJO_PORTAL_CONFIG=/etc/coderdojo_portal/Settings.toml" ];
    Volumes = {
      "/etc/coderdojo_portal" = {};
    };
  };
}