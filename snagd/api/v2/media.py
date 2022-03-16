# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from snagd import task
from snagd.db import schema, session

router = APIRouter()


@router.get("/media", response_model=list[schema.media.Base])
def media(
    categories: Optional[str] = None,
    description: Optional[str] = None,
    source_url: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    uuid: Optional[str] = None,
    db: Session = Depends(session.get_db),
):
    obj: schema.media.Read = schema.media.Read(
        categories=categories,
        description=description,
        source_url=source_url,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
    )
    return task.media.search(obj=obj, db=db)
