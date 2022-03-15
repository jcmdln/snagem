# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from snagd import task
from snagd.db import crud, schema, session

router = APIRouter()


@router.get("/media", response_model=list[schema.media.Base])
def media(db: Session = Depends(session.get_db)):
    return crud.Media().search(db=db)


@router.get("/media/{uuid}", response_model=schema.media.Base)
def media_info(uuid: str, db: Session = Depends(session.get_db)):
    result = crud.Media().get(db=db, uuid=uuid)

    if not result:
        raise HTTPException(status_code=404, detail=f"Media not found: {uuid}")

    return result


@router.post("/media/add", response_model=schema.media.Base)
def media_add(
    source_url: str,
    categories: Optional[str] = None,
    description: Optional[str] = None,
    subtitles: Optional[str] = None,
    tags: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(session.get_db),
):
    obj: schema.media.Create = schema.media.Create(
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )
    return task.media.add(obj, db)
