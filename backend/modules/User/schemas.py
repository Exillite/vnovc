from pydantic import BaseModel
from typing import List


class User(BaseModel):
    nickname: str
    email: str
    password: str
    bio: str
    role: str


class UserCreate(BaseModel):
    nickname: str
    email: str
    password: str
    bio: str


class UserUpdate(BaseModel):
    nickname: str
    email: str
    password: str
    bio: str
