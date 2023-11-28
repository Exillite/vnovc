from modules.User.models import UserModel
from modules.User.schemas import *

from typing import Optional


async def create_user(user: UserCreate) -> UserModel:
    user_model = UserModel(nickname=user.nickname, email=user.email,
                           password=user.password, bio=user.bio, role="user")
    await user_model.create()
    return user_model


async def get_user(user_id: str) -> Optional[UserModel]:
    user = await UserModel.get(id=user_id)
    return user


async def edit_user(user_id: str, user: UserUpdate) -> UserModel:
    user_model = await get_user(user_id)
    if not user_model:
        raise Exception("User not found")
    user_model.nickname = user.nickname
    user_model.bio = user.bio
    await user_model.update()
    return user_model


async def delete_user(user_id: str) -> None:
    user_model = await get_user(user_id)
    if not user_model:
        raise Exception("User not found")
    await user_model.delete()
