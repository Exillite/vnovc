from mangodm import Document
from modules.Node.models import NodeModel

from typing import Dict, List


class SceneModel(Document):
    title: str
    nodes: List[NodeModel]
    data: Dict[str, int]

    class Config:
        collection_name = "scene"


def register_scene_collections():
    SceneModel.register_collection()
