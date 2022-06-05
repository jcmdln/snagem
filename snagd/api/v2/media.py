# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Any, List, Optional

from fastapi import APIRouter

from snagd import config, task
from snagd.db import schema
from snagd.task.session import celery

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
    if config.CELERY_BROKER_URL:
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
