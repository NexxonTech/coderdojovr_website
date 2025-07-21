from typing import Self, Any

from appwrite.client import Client
from appwrite.exception import AppwriteException
from appwrite.services.account import Account
from appwrite.services.users import Users
from flask_login import UserMixin


class User(UserMixin):
    @classmethod
    def try_login(cls, appwrite: Client, email: str, password: str) -> Self:
        account = Account(appwrite)
        users = Users(appwrite)

        new_session = account.create_email_password_session(email, password)
        return cls(users.get(new_session["userId"]))

    @classmethod
    def try_recover(cls, appwrite: Client, userid: str):
        users = Users(appwrite)
        return cls(users.get(userid))

    def __init__(self, appwrite_user: dict[str, Any]):
        super().__init__()

        self.id = appwrite_user["$id"]
        self.name = appwrite_user["name"]
        self.email = appwrite_user["email"]
