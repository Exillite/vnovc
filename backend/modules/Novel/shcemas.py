from pydantic import BaseModel
from typing import List, Dict

from modules.User.schemas import User
from modules.Person.schemas import Person
from modules.Chapter.schemas import Chapter


class Nonel(BaseModel):
    title: str
    description: str
    author: User
    is_public: bool
    persons: List[Person]
    chapters: List[Chapter]
    data: Dict[str, int]


class NonelCreate(BaseModel):
    title: str
    description: str
    author_id: str
    is_public: bool
    persons_ids: List[str]
    chapters_ids: List[str]
    data: Dict[str, int]


class NonelUpdate(BaseModel):
    title: str
    description: str
    author_id: str
    is_public: bool
    persons_ids: List[str]
    chapters_ids: List[str]
    data: Dict[str, int]
