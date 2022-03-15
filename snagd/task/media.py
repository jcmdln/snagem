# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import Depends
from sqlalchemy.orm import Session

from snagd.db import crud, schema, session


def add(obj: schema.media.Create, db: Session = Depends(session.get_db)):
    return crud.Media().create(db=db, obj=obj)


def remove(obj: schema.media.Delete, db: Session = Depends(session.get_db)):
    return crud.Media().delete(db=db, obj=obj)
