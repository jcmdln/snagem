from uuid import uuid4 as new_uuid

from fastapi import APIRouter

from snagem.db.schema import media as schema
from snagem.task import media as task

router = APIRouter()


@router.get("/media", response_model=list[schema.Media])
async def media_search(
    *,
    uuid: str | None = None,
    source_url: str | None = None,
    categories: str | None = None,
    description: str | None = None,
    subtitles: str | None = None,
    tags: str | None = None,
    title: str | None = None,
) -> list[dict]:
    _categories: list[str] | None = categories.split(",") if categories else None
    _subtitles: list[str] | None = subtitles.split(",") if subtitles else None
    _tags: list[str] | None = tags.split(",") if tags else None

    result: list[dict] = task.search.delay(
        uuid=uuid,
        source_url=source_url,
        categories=_categories,
        description=description,
        subtitles=_subtitles,
        tags=_tags,
        title=title,
    ).get()
    return result


@router.post("/media", response_model=schema.Media)
async def media_create(
    *,
    source_url: str | None,
    categories: str | None = None,
    description: str | None = None,
    tags: str | None = None,
    title: str | None = None,
) -> dict:
    _uuid: str = new_uuid().__str__()
    _categories: list[str] | None = categories.split(",") if categories else None
    _tags: list[str] | None = tags.split(",") if tags else None

    result: dict = task.create.delay(
        uuid=_uuid,
        source_url=source_url,
        categories=_categories,
        description=description,
        tags=_tags,
        title=title,
    ).get()
    return result


@router.get("/media/{uuid}", response_model=schema.Media)
async def media_read(uuid: str) -> dict:
    result: dict = task.read.delay(uuid=uuid).get()
    return result


@router.put("/media/{uuid}", response_model=schema.Media)
async def media_update(
    *,
    uuid: str,
    source_url: str | None = None,
    categories: str | None = None,
    description: str | None = None,
    tags: str | None = None,
    title: str | None = None,
) -> dict:
    _categories: list[str] | None = categories.split(",") if categories else None
    _tags: list[str] | None = tags.split(",") if tags else None

    result: dict = task.update.delay(
        uuid=uuid,
        source_url=source_url,
        categories=_categories,
        description=description,
        tags=_tags,
        title=title,
    ).get()
    return result


@router.delete("/media/{uuid}", response_model=schema.Media)
async def media_delete(uuid: str) -> dict:
    result: dict = task.delete.delay(uuid=uuid).get()
    return result


__all__: list[str] = ["router"]
