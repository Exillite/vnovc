from modules.Novel.models import NovelModel
from modules.Novel.shcemas import *

from modules.Person.crud import get_person
from modules.Chapter.crud import get_chapter
from modules.User.crud import get_user

from typing import Optional


async def create_novel(novel: NovelCreate) -> NovelModel:
    author = await get_user(novel.author_id)
    if not author:
        raise ValueError("Author not found")

    persons = []
    for person in novel.persons_ids:
        person_model = await get_person(person)
        if not person_model:
            raise ValueError("Person not found")
        persons.append(person_model)

    chapters = []
    for chapter in novel.chapters_ids:
        chapter_model = await get_chapter(chapter)
        if not chapter_model:
            raise ValueError("Chapter not found")
        chapters.append(chapter_model)

    novel_model = NovelModel(
        title=novel.title,
        description=novel.description,
        author=author,
        is_public=novel.is_public,
        persons=persons,
        chapters=chapters,
        data=novel.data
    )

    await novel_model.create()
    return novel_model


async def get_novel(novel_id: str) -> Optional[NovelModel]:
    novel = await NovelModel.get(id=novel_id)
    return novel


async def edit_novel(novel_id: str, novel: NovelUpdate) -> NovelModel:
    novel_model = await get_novel(novel_id)
    if not novel_model:
        raise Exception("Novel not found")

    persons = []
    for person in novel.persons_ids:
        person_model = await get_person(person)
        if not person_model:
            raise ValueError("Person not found")
        persons.append(person_model)

    chapters = []
    for chapter in novel.chapters_ids:
        chapter_model = await get_chapter(chapter)
        if not chapter_model:
            raise ValueError("Chapter not found")
        chapters.append(chapter_model)

    novel_model.title = novel.title
    novel_model.description = novel.description
    novel_model.is_public = novel.is_public
    novel_model.persons = persons
    novel_model.chapters = chapters
    novel_model.data = novel.data

    await novel_model.update()
    return novel_model


async def delete_novel(novel_id: str) -> None:
    novel = await get_novel(novel_id)
    if not novel:
        raise Exception("Novel not found")

    await novel.delete()
