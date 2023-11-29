from modules.Person.models import PersonModel, SpriteModel
from modules.Person.schemas import *

from typing import Optional


async def create_sprite(sprite: SpriteCreate) -> SpriteModel:
    sprite_model = SpriteModel(
        title=sprite.title,
        image=sprite.image
    )
    await sprite_model.create()
    return sprite_model


async def get_sprite(sprite_id: str) -> Optional[SpriteModel]:
    sprite = await SpriteModel.get(id=sprite_id)
    return sprite


async def edit_sprite(sprite_id: str, sprite: SpriteUpdate) -> SpriteModel:
    sprite_model = await SpriteModel.get(id=sprite_id)
    if not sprite_model:
        raise Exception("Sprite not found")
    sprite_model.title = sprite.title
    sprite_model.image = sprite.image
    await sprite_model.update()
    return sprite_model


async def delete_sprite(sprite_id: str) -> None:
    sprite = await SpriteModel.get(id=sprite_id)
    if not sprite:
        raise Exception("Sprite not found")
    await sprite.delete()


async def create_person(person: PersonCreate) -> PersonModel:
    sprites = []
    for sprite_id in person.sprites_ids:
        sprite = await SpriteModel.get(id=sprite_id)
        if not sprite:
            raise Exception("Sprite not found")
        sprites.append(sprite)

    person_model = PersonModel(
        name=person.name,
        description=person.description,
        data=person.data,
        sprites=sprites
    )
    await person_model.create()
    return person_model


async def get_person(person_id: str) -> Optional[PersonModel]:
    person = await PersonModel.get(id=person_id)
    return person


async def edit_person(person_id: str, person: PersonUpdate) -> PersonModel:
    person_model = await PersonModel.get(id=person_id)
    if not person_model:
        raise Exception("Person not found")

    sprites = []
    for sprite_id in person.sprites_ids:
        sprite = await SpriteModel.get(id=sprite_id)
        if not sprite:
            raise Exception("Sprite not found")
        sprites.append(sprite)

    person_model.name = person.name
    person_model.description = person.description
    person_model.data = person.data
    person_model.sprites = sprites
    await person_model.update()
    return person_model


async def delete_person(person_id: str) -> None:
    person = await PersonModel.get(id=person_id)
    if not person:
        raise Exception("Person not found")
    await person.delete()
