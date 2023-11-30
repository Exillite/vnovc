import re
from tracemalloc import start
from turtle import goto, st
from click import edit
from modules.Person.crud import get_person, get_sprite
from modules.Scene.crud import get_scene
from modules.Node.models import *
from modules.Node.schemas import *

from typing import Optional


async def create_node(node: create_nodes_type) -> NodeModel:
    if isinstance(node, StartNodeCreate):
        start_node_model = StartNodeModel(next_node_id=node.next_node_id)
        await start_node_model.create()
        node_model = NodeModel(node_type="start", node_id=start_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, BackgroundNodeCreate):
        background_node_model = BackgroundNodeModel(
            background=node.background, next_node_id=node.next_node_id)
        await background_node_model.create()
        node_model = NodeModel(node_type="background",
                               node_id=background_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, SpeechNodeCreate):
        person = await get_person(node.person_id)
        if not person:
            raise Exception("Person not found")
        sprite = await get_sprite(node.sprite_id)
        if not sprite:
            raise Exception("Sprite not found")
        speech_node_model = SpeechNodeModel(
            person=person, sprite=sprite, text=node.text, next_node_id=node.next_node_id)
        await speech_node_model.create()
        node_model = NodeModel(
            node_type="speech", node_id=speech_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, ChooseNodeCreate):
        answers = []
        for answer in node.answers:
            answer_model = ChooseNodeAnswerModel(
                text=answer.text, next_node_id=answer.next_node_id)
            answers.append(answer_model)

        choose_node_model = ChooseNodeModel(text=node.text, answers=answers)
        await choose_node_model.create()

        node_model = NodeModel(
            node_type="choose", node_id=choose_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, LogicNodeCreate):
        person = None
        if node.person_id:
            person = await get_person(node.person_id)
        logic_node_model = LogicNodeModel(
            data_directory=node.data_directory,
            person=person,
            variable=node.variable,
            condition=node.condition,
            if_node_id=node.if_node_id,
            else_node_id=node.else_node_id
        )
        await logic_node_model.create()
        node_model = NodeModel(node_type="logic", node_id=logic_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, EditVariableNodeCreate):
        person = None
        if node.person_id:
            person = await get_person(node.person_id)
        edit_variable_node_model = EditVariableNodeModel(
            data_directory=node.data_directory,
            person=person,
            variable=node.variable,
            update_variable=node.update,
            next_node_id=node.next_node_id
        )
        await edit_variable_node_model.create()
        node_model = NodeModel(node_type="edit_variable",
                               node_id=edit_variable_node_model.id)
        await node_model.create()
        return node_model
    elif isinstance(node, GotoSceneNodeCreate):
        scene = await get_scene(node.scene_id)
        if not scene:
            raise Exception("Scene not found")
        goto_scene_node_model = GotoSceneNodeModel(scene=scene)
        await goto_scene_node_model.create()
        node_model = NodeModel(node_type="goto_scene",
                               node_id=goto_scene_node_model.id)
        await node_model.create()
        return node_model
    else:
        raise Exception("Unknown node type")


async def get_node(node_id: str) -> Optional[NodeModel]:
    node_model = await NodeModel.get(id=node_id)
    return node_model


async def edit_node(node_id: str, node: update_nodes_type) -> NodeModel:
    node_model = await get_node(node_id)
    if not node_model:
        raise Exception("Node not found")
    if node_model.node_type == "start":
        if not isinstance(node, StartNodeUpdate):
            raise Exception("Invalid node type")
        start_node_model = await StartNodeModel.get(id=node_model.node_id)
        if not start_node_model:
            raise Exception("Start node not found")
        start_node_model.next_node_id = node.next_node_id
        await start_node_model.update()
        return node_model
    elif node_model.node_type == "background":
        if not isinstance(node, BackgroundNodeUpdate):
            raise Exception("Invalid node type")
        background_node_model = await BackgroundNodeModel.get(
            id=node_model.node_id)
        if not background_node_model:
            raise Exception("Background node not found")
        background_node_model.background = node.background
        background_node_model.next_node_id = node.next_node_id
        await background_node_model.update()
        return node_model
    elif node_model.node_type == "speech":
        if not isinstance(node, SpeechNodeUpdate):
            raise Exception("Invalid node type")
        speech_node_model = await SpeechNodeModel.get(id=node_model.node_id)
        if not speech_node_model:
            raise Exception("Speech node not found")
        person = await get_person(node.person_id)
        if not person:
            raise Exception("Person not found")
        sprite = await get_sprite(node.sprite_id)
        if not sprite:
            raise Exception("Sprite not found")
        speech_node_model.person = person
        speech_node_model.sprite = sprite
        speech_node_model.text = node.text
        speech_node_model.next_node_id = node.next_node_id
        await speech_node_model.update()
        return node_model
    elif node_model.node_type == "choose":
        if not isinstance(node, ChooseNodeUpdate):
            raise Exception("Invalid node type")
        choose_node_model = await ChooseNodeModel.get(id=node_model.node_id)
        if not choose_node_model:
            raise Exception("Choose node not found")
        choose_node_model.text = node.text
        answers = []
        for answer in node.answers:
            answer_model = ChooseNodeAnswerModel(
                text=answer.text, next_node_id=answer.next_node_id)
            answers.append(answer_model)
        choose_node_model.answers = answers
        await choose_node_model.update()
        return node_model
    elif node_model.node_type == "logic":
        if not isinstance(node, LogicNodeUpdate):
            raise Exception("Invalid node type")
        logic_node_model = await LogicNodeModel.get(id=node_model.node_id)
        if not logic_node_model:
            raise Exception("Logic node not found")
        person = None
        if node.person_id:
            person = await get_person(node.person_id)
        logic_node_model.data_directory = node.data_directory
        logic_node_model.person = person
        logic_node_model.variable = node.variable
        logic_node_model.condition = node.condition
        logic_node_model.if_node_id = node.if_node_id
        logic_node_model.else_node_id = node.else_node_id
        await logic_node_model.update()
        return node_model
    if node_model.node_type == "edit_variable":
        if not isinstance(node, EditVariableNodeUpdate):
            raise Exception("Invalid node type")
        edit_variable_node_model = await EditVariableNodeModel.get(
            id=node_model.node_id)
        if not edit_variable_node_model:
            raise Exception("Edit variable node not found")
        person = None
        if node.person_id:
            person = await get_person(node.person_id)
        edit_variable_node_model.data_directory = node.data_directory
        edit_variable_node_model.person = person
        edit_variable_node_model.variable = node.variable
        edit_variable_node_model.update_variable = node.update
        edit_variable_node_model.next_node_id = node.next_node_id
        await edit_variable_node_model.update()
        return node_model
    elif node_model.node_type == "goto_scene":
        if not isinstance(node, GotoSceneNodeUpdate):
            raise Exception("Invalid node type")
        goto_scene_node_model = await GotoSceneNodeModel.get(
            id=node_model.node_id)
        if not goto_scene_node_model:
            raise Exception("Goto scene node not found")
        scene = await get_scene(node.scene_id)
        if not scene:
            raise Exception("Scene not found")
        goto_scene_node_model.scene = scene
        await goto_scene_node_model.update()
        return node_model
    else:
        raise Exception("Unknown node type")


async def delete_node(node_id: str) -> None:
    node_model = await get_node(node_id)
    if not node_model:
        raise Exception("Node not found")
    if node_model.node_type == "start":
        start_node_model = await StartNodeModel.get(id=node_model.node_id)
        if not start_node_model:
            raise Exception("Start node not found")
        await start_node_model.delete()
    elif node_model.node_type == "background":
        background_node_model = await BackgroundNodeModel.get(
            id=node_model.node_id)
        if not background_node_model:
            raise Exception("Background node not found")
        await background_node_model.delete()
    elif node_model.node_type == "speech":
        speech_node_model = await SpeechNodeModel.get(id=node_model.node_id)
        if not speech_node_model:
            raise Exception("Speech node not found")
        await speech_node_model.delete()
    elif node_model.node_type == "choose":
        choose_node_model = await ChooseNodeModel.get(id=node_model.node_id)
        if not choose_node_model:
            raise Exception("Choose node not found")
        await choose_node_model.delete()
    elif node_model.node_type == "logic":
        logic_node_model = await LogicNodeModel.get(id=node_model.node_id)
        if not logic_node_model:
            raise Exception("Logic node not found")
        await logic_node_model.delete()
    elif node_model.node_type == "edit_variable":
        edit_variable_node_model = await EditVariableNodeModel.get(
            id=node_model.node_id)
        if not edit_variable_node_model:
            raise Exception("Edit variable node not found")
        await edit_variable_node_model.delete()
    elif node_model.node_type == "goto_scene":
        goto_scene_node_model = await GotoSceneNodeModel.get(
            id=node_model.node_id)
        if not goto_scene_node_model:
            raise Exception("Goto scene node not found")
        await goto_scene_node_model.delete()
    else:
        raise Exception("Unknown node type")
    await node_model.delete()
