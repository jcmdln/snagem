# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Any, Optional

from fastapi.encoders import jsonable_encoder

from snagd.db import crud, model, schema, session
from snagd.task.session import celery


@celery.task(name="snagd.media.add")
def add(
    source_url: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
) -> Optional[model.Media] | Any:
    obj: schema.MediaCreate = schema.MediaCreate(
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )

    result = crud.Media().create(db=session.SessionLocal(), obj=obj)
    if result:
        return jsonable_encoder(result)

    return None


@celery.task(name="snagd.media.get")
def get(uuid: str) -> Optional[model.Media] | Any:
    result = crud.Media().get(db=session.SessionLocal(), uuid=uuid)
    if result:
        return jsonable_encoder(result)

    return None


@celery.task(name="snagd.media.remove")
def remove(uuid: str) -> Optional[model.Media] | Any:
    obj: schema.MediaDelete = schema.MediaDelete(uuid=uuid)
    result = crud.Media().delete(db=session.SessionLocal(), obj=obj)
    if result:
        return jsonable_encoder(result)

    return None


@celery.task(name="snagd.media.search")
def search(
    categories: Optional[str] = None,
    description: Optional[str] = None,
    source_url: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    uuid: Optional[str] = None,
) -> list[model.Media] | list[dict]:
    obj: schema.MediaRead = schema.MediaRead(
        categories=categories,
        description=description,
        source_url=source_url,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
    )

    result: list[dict] = []
    for item in crud.Media().search(db=session.SessionLocal(), obj=obj):
        result.append(jsonable_encoder(item))

    return result


@celery.task(name="snagd.media.update")
def update(
    uuid: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
) -> Optional[model.Media] | Any:
    obj: schema.MediaUpdate = schema.MediaUpdate(
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )

    result = crud.Media().update(db=session.SessionLocal(), obj=obj, uuid=uuid)
    if result:
        return jsonable_encoder(result)

    return None


__all__: list[str] = ["add", "get", "remove", "search", "update"]
