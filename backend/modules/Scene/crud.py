from modules.Scene.models import SceneModel
from modules.Scene.schemas import *

from typing import Optional


async def create_scene(scene: SceneCreate) -> SceneModel:
    scene_model = SceneModel(title=scene.title, nodes=[], data={})
    await scene_model.create()
    return scene_model


async def get_scene(scene_id: str) -> Optional[SceneModel]:
    scene_model = await SceneModel.get(id=scene_id)
    return scene_model


async def edit_scene(scene_id: str, scene: SceneUpdate) -> SceneModel:
    scene_model = await SceneModel.get(id=scene_id)
    if not scene_model:
        raise Exception("Scene not found")

    scene_model.title = scene.title
    scene_model.data = scene.data

    await scene_model.update()
    return scene_model


async def delete_scene(scene_id: str) -> None:
    scene = await SceneModel.get(id=scene_id)
    if not scene:
        raise Exception("Scene not found")
    await scene.delete()
