# SPDX-License-Identifier: AGPL-3.0-or-later
from typing import Generic, Optional, Type, TypeVar
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from snagd.db import session

ModelType = TypeVar("ModelType", bound=session.Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
DeleteSchemaType = TypeVar("DeleteSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class Base(Generic[ModelType, CreateSchemaType, DeleteSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, obj: CreateSchemaType) -> Optional[ModelType]:
        obj_data = jsonable_encoder(obj)
        db_obj: ModelType = self.model(**obj_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db: Session, obj: DeleteSchemaType) -> Optional[ModelType]:
        obj_data: Optional[ModelType] = db.query(self.model).get(obj)

        if obj:
            db.delete(obj_data)
            db.commit()

        return obj_data

    def get(self, db: Session, uuid: UUID) -> Optional[ModelType]:
        result: ModelType = db.query(self.model).filter(self.model.uuid == uuid).first()
        return result

    def update(self, db: Session, db_obj: ModelType, obj: UpdateSchemaType) -> Optional[ModelType]:
        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj, dict):
            update_data = obj
        else:
            update_data = obj.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj


__all__: list[str] = ["Base"]
