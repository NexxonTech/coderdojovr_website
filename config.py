import os, tomllib


class Config:
    config: dict = {}

    @classmethod
    def get(cls, profile: str) -> dict:
        config_path = os.getenv('CODERDOJO_PORTAL_CONFIG', './Settings.' + profile + '.toml')

        if cls.config.get(profile) is None:
            with open(config_path, "rb") as settings_file:
                cls.config[profile] = tomllib.load(settings_file)
        return cls.config[profile]
