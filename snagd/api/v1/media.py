# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Any, List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from snagd import task
from snagd.db import model, schema, session

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
    db: Session = Depends(session.get),
) -> Optional[List[model.Media]] | Any:
    return task.media.search(
        categories=categories,
        description=description,
        source_url=source_url,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
        db=db,
    )


@router.get("/media/{uuid}", response_model=schema.Media)
def media_get(uuid: str, db: Session = Depends(session.get)) -> Optional[model.Media] | Any:
    """Get a Media object by uuid."""
    return task.media.get(uuid=uuid, db=db)


@router.post("/media/add", response_model=schema.Media)
def media_add(
    source_url: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(session.get),
) -> Optional[model.Media] | Any:
    return task.media.add(
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
        db=db,
    )


@router.delete("/media/remove", response_model=schema.Media)
def media_remove(uuid: str, db: Session = Depends(session.get)) -> Optional[model.Media] | Any:
    return task.media.remove(uuid=uuid, db=db)


@router.put("/media/update", response_model=schema.Media)
def media_update(
    uuid: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(session.get),
) -> Optional[model.Media] | Any:
    return task.media.update(
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
        db=db,
    )
