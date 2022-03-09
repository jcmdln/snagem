# SPDX-License-Identifier: AGPL-3.0-or-later
from typing import Generic, Optional, Type, TypeVar
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from snagd.db import session

Model = TypeVar("Model", bound=session.Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
DeleteSchema = TypeVar("DeleteSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class Base(Generic[Model, CreateSchema, DeleteSchema, UpdateSchema]):
    def __init__(self, model: Type[Model]):
        self.model = model

    def get(self, db: Session, uuid: UUID) -> Optional[Model]:
        return db.query(self.model).filter(self.model.uuid == uuid).first()

    #
    # CRUD
    #

    def create(self, db: Session, obj: CreateSchema) -> Optional[Model]:
        obj_data = jsonable_encoder(obj)
        db_obj: Model = self.model(**obj_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, obj: DeleteSchema) -> Optional[Model]:
        obj_data: Optional[Model] = db.query(self.model).get(obj)

        if obj:
            db.delete(obj_data)
            db.commit()

        return obj_data

    def update(self, db: Session, obj: UpdateSchema) -> Optional[Model]:
        obj_data = jsonable_encoder(self.model)
        update_data = obj.dict()
        for field in obj_data:
            if field in update_data:
                setattr(obj_data, field, update_data[field])

        db_obj: Optional[Model] = self.model(**obj_data)
        if db_obj:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        return db_obj


__all__: list[str] = ["Base"]
