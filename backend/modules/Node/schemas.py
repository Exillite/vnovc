from pydantic import BaseModel
from typing import List, Optional, Union

from modules.Person.schemas import Person, Sprite
from modules.Scene.schemas import Scene


class Node(BaseModel):
    id: str
    node_type: str
    node: Union["StartNode", "BackgroundNode", "SpeechNode",
                "ChooseNode", "LogicNode", "EditVariableNode", "GotoSceneNode"]


class NodeCreate(BaseModel):
    node_type: str
    node_id: str


class StartNode(BaseModel):
    next_node_id: str


class StartNodeCreate(BaseModel):
    next_node_id: str


class StartNodeUpdate(BaseModel):
    next_node_id: str


class BackgroundNode(BaseModel):
    background: str
    next_node_id: str


class BackgroundNodeCreate(BaseModel):
    background: str
    next_node_id: str


class BackgroundNodeUpdate(BaseModel):
    background: str
    next_node_id: str


class SpeechNode(BaseModel):
    person: Person
    sprite: Sprite
    text: str
    next_node_id: str


class SpeechNodeCreate(BaseModel):
    person_id: str
    sprite_id: str
    text: str
    next_node_id: str


class SpeechNodeUpdate(BaseModel):
    person_id: str
    sprite_id: str
    text: str
    next_node_id: str


class ChooseNodeAnswer(BaseModel):
    text: str
    next_node_id: str


class ChooseNode(BaseModel):
    text: str
    answers: List[ChooseNodeAnswer]


class ChooseNodeCreate(BaseModel):
    text: str
    answers: List[ChooseNodeAnswer]


class ChooseNodeUpdate(BaseModel):
    text: str
    answers: List[ChooseNodeAnswer]


class LogicNode(BaseModel):
    data_directory: str
    person: Optional[Person]
    variable: str
    condition: str
    if_node_id: str
    else_node_id: str


class LogicNodeCreate(BaseModel):
    data_directory: str
    person_id: Optional[str]
    variable: str
    condition: str
    if_node_id: str
    else_node_id: str


class LogicNodeUpdate(BaseModel):
    data_directory: str
    person_id: Optional[str]
    variable: str
    condition: str
    if_node_id: str
    else_node_id: str


class EditVariableNode(BaseModel):
    data_directory: str
    person: Optional[Person]
    variable: str
    update: str
    next_node_id: str


class EditVariableNodeCreate(BaseModel):
    data_directory: str
    person_id: Optional[str]
    variable: str
    update: str
    next_node_id: str


class EditVariableNodeUpdate(BaseModel):
    data_directory: str
    person_id: Optional[str]
    variable: str
    update: str
    next_node_id: str


class GotoSceneNode(BaseModel):
    scene: Scene


class GotoSceneNodeCreate(BaseModel):
    scene_id: str


class GotoSceneNodeUpdate(BaseModel):
    scene_id: str
