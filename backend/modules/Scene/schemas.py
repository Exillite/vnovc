from pydantic import BaseModel
from typing import Dict, List

from modules.Node.schemas import Node


class Scene(BaseModel):
    title: str
    nodes: List[Node]
    data: Dict[str, int]


class SceneCreate(BaseModel):
    title: str
    data: Dict[str, int]


class SceneUpdate(BaseModel):
    title: str
    data: Dict[str, int]
