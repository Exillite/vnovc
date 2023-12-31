from mangodm import Document, EmbeddedDocument
from typing import List, Optional

from modules.Person.models import PersonModel, SpriteModel
from modules.Scene.models import SceneModel

"""
start
background
speech
choose
logic
edit_variable
goto_scene
"""

class NodeModel(Document):
    node_type: str
    node_id: str

    class Config:
        collection_name = "node"


class StartNodeModel(Document):
    next_node_id: str

    class Config:
        collection_name = "start_node"


class BackgroundNodeModel(Document):
    background: str
    next_node_id: str

    class Config:
        collection_name = "background_node"


class SpeechNodeModel(Document):
    person: PersonModel
    sprite: SpriteModel
    text: str
    next_node_id: str

    class Config:
        collection_name = "speech_node"


class ChooseNodeModel(Document):
    text: str
    answers: List["ChooseNodeAnswerModel"]

    class Config:
        collection_name = "choose_node"


class ChooseNodeAnswerModel(EmbeddedDocument):
    text: str
    next_node_id: str


class LogicNodeModel(Document):
    data_directory: str
    person: Optional[PersonModel]
    variable: str
    condition: str
    if_node_id: str
    else_node_id: str

    class Config:
        collection_name = "logic_node"


class EditVariableNodeModel(Document):
    data_directory: str
    person: Optional[PersonModel]
    variable: str
    update_variable: str
    next_node_id: str

    class Config:
        collection_name = "edit_variable_node"


class GotoSceneNodeModel(Document):
    scene: SceneModel


def register_node_collections():
    NodeModel.register_collection()
    StartNodeModel.register_collection()
    BackgroundNodeModel.register_collection()
    SpeechNodeModel.register_collection()
    ChooseNodeModel.register_collection()
    ChooseNodeAnswerModel.register_embedded_collection()
    LogicNodeModel.register_collection()
    EditVariableNodeModel.register_collection()
    GotoSceneNodeModel.register_collection()
