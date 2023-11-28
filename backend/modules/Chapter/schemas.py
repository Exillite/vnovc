from pydantic import BaseModel
from typing import List

from modules.Scene.schemas import Scene


class Chapter(BaseModel):
    id: str
    title: str
    scenes: Scene


class ChapterCreate(BaseModel):
    title: str


class ChapterUpdate(BaseModel):
    title: str
