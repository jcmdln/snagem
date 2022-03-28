# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from snagd.db import crud, model, schema, session


# snagd.task.media.add
def add(
    source_url: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(session.get),
) -> Optional[model.Media]:
    obj: schema.MediaCreate = schema.MediaCreate(
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )
    return crud.Media().create(db=db, obj=obj)


# snagd.task.media.get
def get(uuid: str, db: Session = Depends(session.get)) -> Optional[model.Media]:
    return crud.Media().get(db=db, uuid=uuid)


# snagd.task.media.remove
def remove(uuid: str, db: Session = Depends(session.get)) -> Optional[model.Media]:
    obj: schema.MediaDelete = schema.MediaDelete(uuid=uuid)
    return crud.Media().delete(db=db, obj=obj)


# snagd.task.media.search
def search(
    categories: Optional[str] = None,
    description: Optional[str] = None,
    source_url: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    uuid: Optional[str] = None,
    db: Session = Depends(session.get),
) -> Optional[list[model.Media]]:
    obj: schema.MediaRead = schema.MediaRead(
        categories=categories,
        description=description,
        source_url=source_url,
        subtitles=subtitles,
        tags=tags,
        title=title,
        uuid=uuid,
    )
    return crud.Media().search(db=db, obj=obj)


# snagd.task.media.update
def update(
    uuid: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(session.get),
) -> Optional[model.Media]:
    obj: schema.MediaUpdate = schema.MediaUpdate(
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )
    return crud.Media().update(db=db, obj=obj, uuid=uuid)


__all__: list[str] = ["add", "get", "remove", "search", "update"]
