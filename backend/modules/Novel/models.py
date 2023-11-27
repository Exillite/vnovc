from mangodm import Document
from modules.User.models import UserModel
from modules.Person.models import PersonModel
from modules.Chapter.models import ChapterModel

from typing import Dict, List


class NovelModel(Document):
    title: str
    description: str
    author: UserModel
    is_public: bool
    persons: List[PersonModel]
    chapters: List[ChapterModel]
    data: Dict[str, int]

    class Config:
        collection_name = "novel"
