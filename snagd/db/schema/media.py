# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Create(BaseModel):
    source_url: str

    categories: Optional[list[str]]
    description: Optional[str]
    tags: Optional[list[str]]
    title: Optional[str]


class Delete(BaseModel):
    uuid: str


class Update(BaseModel):
    categories: Optional[list[str]]
    description: Optional[str]
    subtitles: Optional[list[str]]
    tags: Optional[list[str]]
    title: Optional[str]


class Read(Update):
    date_created: Optional[datetime]
    date_updated: Optional[datetime]
    duration: Optional[int]
    source_url: Optional[str]
    title: Optional[str]
    uuid: Optional[str]
    views: Optional[int]


class Base(Create, Delete, Update):
    date_created: datetime
    date_updated: datetime
    duration: int
    title: str
    views: int

    class Config:
        orm_mode = True


__all__: list[str] = ["Base", "Create", "Delete", "Read", "Update"]
