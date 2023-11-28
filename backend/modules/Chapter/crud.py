from modules.Chapter.models import ChapterModel
from modules.Chapter.schemas import *

from typing import List, Optional


async def create_chapter(nc: ChapterCreate) -> ChapterModel:
    c = ChapterModel(title=nc.title, scenes=[])
    await c.create()
    return c


async def get_chapter(chapter_id: str) -> Optional[ChapterModel]:
    c = await ChapterModel.get(id=chapter_id)
    return c


async def edit_chapter(chapter_id: str, nc: ChapterUpdate) -> ChapterModel:
    c = await ChapterModel.get(id=chapter_id)
    if not c:
        raise ValueError("Chapter not found")
    c.title = nc.title
    await c.update()
    return c


async def delete_chapter(chapter_id: str) -> None:
    c = await ChapterModel.get(id=chapter_id)
    if not c:
        raise ValueError("Chapter not found")
    await c.delete()
