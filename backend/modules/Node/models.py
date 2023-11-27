from mangodm import Document, EmbeddedDocument
from typing import List, Optional

from modules.Person.models import PersonModel, SpriteModel
from modules.Scene.models import SceneModel


class NodeModel(Document):
    node_type: str
    node_id: str

    class Config:
        collection_name = "node"


class StartNodeModel(Document):
    next_node: NodeModel

    class Config:
        collection_name = "start_node"


class BackgroundNodeModel(Document):
    background: str
    next_node: NodeModel

    class Config:
        collection_name = "background_node"


class SpeechNodeModel(Document):
    person: PersonModel
    sprite: SpriteModel
    text: str
    next_node: NodeModel

    class Config:
        collection_name = "speech_node"


class ChooseNodeModel(Document):
    text: str
    answers: List["ChooseNodeAnswerModel"]

    class Config:
        collection_name = "choose_node"


class ChooseNodeAnswerModel(EmbeddedDocument):
    text: str
    next_node: NodeModel


class LogicNodeModel(Document):
    data_directory: str
    person: Optional[PersonModel]
    variable: str
    condition: str
    if_node: NodeModel
    else_node: NodeModel

    class Config:
        collection_name = "logic_node"


class EditVariableNode(Document):
    data_directory: str
    person: Optional[PersonModel]
    variable: str
    update: str

    class Config:
        collection_name = "edit_variable_node"


class GotoSceneNode(Document):
    scene: SceneModel


def register_node_collections():
    NodeModel.register_collection()
    StartNodeModel.register_collection()
    BackgroundNodeModel.register_collection()
    SpeechNodeModel.register_collection()
    ChooseNodeModel.register_collection()
    ChooseNodeAnswerModel.register_embedded_collection()
    LogicNodeModel.register_collection()
    EditVariableNode.register_collection()
    GotoSceneNode.register_collection()
