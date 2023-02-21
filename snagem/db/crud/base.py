# SPDX-License-Identifier: AGPL-3.0-or-later

from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from snagem.db.schema.base import Base as Schema
from snagem.db.session import Base as BaseModel

Model = TypeVar("Model", bound=BaseModel)
Create = TypeVar("Create", bound=Schema)
Delete = TypeVar("Delete", bound=Schema)
Read = TypeVar("Read", bound=Schema)
Update = TypeVar("Update", bound=Schema)


class Base(Generic[Model, Create, Delete, Read, Update]):
    def __init__(self, model: type[Model]) -> None:
        self.model: type[Model] = model

    def create(self, db: Session, obj: Create) -> Model | None:
        db_obj: Model = self.model(**obj.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        db.close()
        return db_obj

    def delete(self, db: Session, obj: Delete) -> Model | None:
        query: Model | None = db.get(self.model, obj.dict())
        if query:
            db.delete(query)
            db.commit()

        db.close()
        return query

    def read(self, db: Session, uuid: str) -> Model | None:
        result: Model | None = db.query(self.model).filter_by(uuid=uuid).first()
        db.close()
        return result

    def search(self, db: Session, obj: Read, limit: int = 100, skip: int = 0) -> list[Model]:
        query = db.query(self.model)
        for k, v in obj.dict().items():
            if v:
                query = query.filter(getattr(self.model, k) == v)

        result: list[Model] = query.offset(skip).limit(limit).all()
        db.close()
        return result

    def update(self, db: Session, obj: Update, uuid: str) -> Model | None:
        query: Model | None = self.read(db=db, uuid=uuid)
        update_data = obj.dict()

        for field in Schema.from_orm(query).dict():
            if field in update_data:
                setattr(query, field, update_data[field])

        db.add(query)
        db.commit()
        db.refresh(query)
        db.close()
        return query


__all__: list[str] = ["Base"]
