from datetime import datetime

from snagem.db.schema.base import Base


class Update(Base):
    source_url: str | None
    categories: list[str] | None
    description: str | None
    tags: list[str] | None
    title: str | None


class Delete(Base):
    uuid: str


class Create(Delete, Update):
    source_url: str


class Read(Update):
    uuid: str | None


class Media(Create):
    duration: int

    subtitles: list[str] | None
    views: int

    date_created: datetime
    date_updated: datetime


__all__: list[str] = ["Media", "Create", "Delete", "Read", "Update"]
