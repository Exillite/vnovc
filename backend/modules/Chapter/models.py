from mangodm import Document
from modules.Scene.models import SceneModel

from typing import List


class ChapterModel(Document):
    title: str
    scenes: List[SceneModel]

    class Config:
        collection_name = "chapter"
        
        
def register_chapter_collections():
    ChapterModel.register_collection()
