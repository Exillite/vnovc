from pydantic import BaseModel
from typing import List, Dict


class Sprite(BaseModel):
    title: str
    image: str


class SpriteCreate(BaseModel):
    title: str
    image: str


class SpriteUpdate(BaseModel):
    title: str
    image: str


class Person(BaseModel):
    name: str
    description: str
    data: Dict[str, int]
    sprites: List[Sprite]


class PersonCreate(BaseModel):
    name: str
    description: str
    data: Dict[str, int]
    sprites_ids: List[str]


class PersonUpdate(BaseModel):
    name: str
    description: str
    data: Dict[str, int]
    sprites_ids: List[str]
