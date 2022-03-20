# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from snagd.db import session

Model = TypeVar("Model", bound=session.Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
DeleteSchema = TypeVar("DeleteSchema", bound=BaseModel)
ReadSchema = TypeVar("ReadSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class Base(Generic[Model, CreateSchema, DeleteSchema, ReadSchema, UpdateSchema]):
    def __init__(self, model: Type[Model]) -> None:
        self.model: Type[Model] = model

    def create(self, db: Session, obj: CreateSchema) -> Optional[Model]:
        obj_data = jsonable_encoder(obj)
        db_obj: Model = self.model(**obj_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, obj: DeleteSchema) -> Optional[Model]:
        obj_data = jsonable_encoder(obj)
        db_data: Optional[Model] = db.query(self.model).get(obj_data)

        if db_data:
            db.delete(db_data)
            db.commit()

        return db_data

    def get(self, db: Session, uuid: str) -> Optional[Model]:
        result: Optional[Model] = db.query(self.model).filter_by(uuid=uuid).first()
        return result

    def search(self, db: Session, obj: ReadSchema, limit: int = 100, skip: int = 0) -> list[Model]:
        obj_data: dict = obj.dict()
        query = db.query(self.model)

        for k, v in obj_data.items():
            if v:
                query = query.filter(getattr(self.model, k) == v)

        result: list[Model] = query.offset(skip).limit(limit).all()
        return result

    def update(self, db: Session, obj: UpdateSchema, uuid: str) -> Optional[Model]:
        media_item: Optional[Model] = self.get(db=db, uuid=uuid)
        obj_data = jsonable_encoder(media_item)
        update_data = obj.dict()

        for field in obj_data:
            if field in update_data:
                setattr(media_item, field, update_data[field])

        db.add(media_item)
        db.commit()
        db.refresh(media_item)

        return media_item


__all__: list[str] = ["Base"]
