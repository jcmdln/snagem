# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import Depends
from sqlalchemy.orm import Session

from snagd.db import crud, schema, session


# task.media.add
def add(obj: schema.media.Create, db: Session = Depends(session.get_db)):
    return crud.Media().create(db=db, obj=obj)


# task.media.remove
def remove(obj: schema.media.Delete, db: Session = Depends(session.get_db)):
    return crud.Media().delete(db=db, obj=obj)


# task.media.info(obj=obj, db=db)
def info(uuid: str, db: Session = Depends(session.get_db)):
    return crud.Media().get(db=db, uuid=uuid)


# task.media.search
def search(obj: schema.media.Read, db: Session = Depends(session.get_db)):
    return crud.Media().search(db=db, obj=obj)


# task.media.update
def update(obj: schema.media.Update, db: Session = Depends(session.get_db)):
    return crud.Media().update(db=db, obj=obj)
