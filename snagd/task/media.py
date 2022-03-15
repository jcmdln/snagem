# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Optional

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from snagd.db import crud, model, schema, session


def add(obj: schema.media.Create, db: Session = Depends(session.get_db)):
    db_obj: Optional[model.Media] = crud.Media().create(db=db, obj=obj)

    if not db_obj:
        raise HTTPException(500, f"Failed to create media object from {obj.source_url}")

    return db_obj
