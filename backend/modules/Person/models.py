from mangodm import Document

from typing import Dict, List


class PersonModel(Document):
    name: str
    description: str
    data: Dict[str, int]
    sprites: List["SpriteModel"]

    class Config:
        collection_name = "person"


class SpriteModel(Document):
    title: str
    image: str

    class Config:
        collection_name = "sprite"
