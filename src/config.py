import os, tomllib


class Config:
    read: bool = False
    config: dict

    @classmethod
    def get(cls) -> dict:
        config_path = os.getenv('CODERDOJO_PORTAL_CONFIG', './Settings.toml')

        if not cls.read:
            with open(config_path, "rb") as settings_file:
                cls.config = tomllib.load(settings_file)
                cls.read = True
        return cls.config