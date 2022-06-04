# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Any, List, Optional

from fastapi import APIRouter

from snagd import config, task
from snagd.db import model, schema
from snagd.task import celery

router = APIRouter()


@router.get("/media", response_model=List[schema.Media])
def media(
    categories: Optional[str] = None,
    description: Optional[str] = None,
    source_url: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    uuid: Optional[str] = None,
) -> list[schema.Media] | Any:
    if config.broker_url:
        return celery.send_task(
            "snagd.media.search",
            args=[categories, description, source_url, subtitles, tags, title, uuid],
        ).get()

    return task.media.search(
        categories=categories,
        description=description,
        source_url=source_url,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
    )


@router.get("/media/{uuid}", response_model=schema.Media)
def media_get(uuid: str) -> Optional[model.Media] | Any:
    """Get a Media object by uuid."""
    if config.broker_url:
        return celery.send_task("snagd.media.get", args=[uuid]).get()

    return task.media.get(uuid=uuid)


@router.post("/media/add", response_model=schema.Media)
def media_add(
    source_url: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
) -> Optional[model.Media] | Any:
    if config.broker_url:
        return celery.send_task(
            "snagd.media.add",
            args=[source_url, categories, description, subtitles, tags, title],
        ).get()

    return task.media.add(
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )


@router.delete("/media/remove", response_model=schema.Media)
def media_remove(uuid: str) -> Optional[model.Media] | Any:
    if config.broker_url:
        return celery.send_task("snagd.media.remove", args=[uuid]).get()

    return task.media.remove(uuid=uuid)


@router.put("/media/update", response_model=schema.Media)
def media_update(
    uuid: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
) -> Optional[model.Media] | Any:
    if config.broker_url:
        return celery.send_task(
            "snagd.media.update",
            args=[categories, description, subtitles, tags, title, uuid],
        ).get()

    return task.media.update(
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
    )
