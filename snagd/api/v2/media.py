# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from snagd.db import crud, schema, session

router = APIRouter()


@router.get("/media", response_model=list[schema.media.Base])
def media(db: Session = Depends(session.get_db)):
    return crud.Media().search(db=db)
