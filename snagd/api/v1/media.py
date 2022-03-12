# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from snagd.db import crud, model, schema, session

router = APIRouter()


@router.get("/media", response_model=list[schema.media.Base])
def media(db: Session = Depends(session.get_db)):
    return crud.Media(model.Media).search(db=db)


@router.get("/media/{uuid}", response_model=schema.media.Base)
def media_info(uuid: str, db: Session = Depends(session.get_db)) -> dict:
    return crud.Media(model.Media).get(db=db, uuid=uuid)


@router.post("/media/add", response_model=schema.media.Base)
def media_add(source_url: str, db: Session = Depends(session.get_db)) -> dict:
    obj = schema.media.Create(source_url=source_url)
    return crud.Media(model.Media).create(db=db, obj=obj)


@router.delete("/media/remove")
def media_remove(uuid: str) -> dict:
    return {
        "uuid": uuid,
    }


@router.put("/media/update", response_model=schema.media.Base)
def media_update(uuid: str) -> dict:
    return {
        "uuid": uuid,
    }
