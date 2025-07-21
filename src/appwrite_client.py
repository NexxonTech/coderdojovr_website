from appwrite.client import Client
from flask import g

from src.config import Config


class AppwriteClient:
    initialized: bool = False
    client: Client

    @classmethod
    def get(cls) -> Client:
        if not cls.initialized:
            appwrite_conf = Config.get()["appwrite"]

            cls.client = Client()
            cls.client.set_endpoint(appwrite_conf["endpoint"]).set_project(appwrite_conf["project"]).set_key(appwrite_conf["key"])

            cls.initialized = True
        return cls.client

    @classmethod
    def load(cls):
        g.appwrite = cls.get()
