from mangodm import Document
from typing import List


class UserModel(Document):
    nickname: str
    email: str
    password: str
    bio: str
    role: str

    class Config:
        collection_name = "user"
        excludeFieldsResponse = ["password"]


def register_user_collections():
    UserModel.register_collection()
