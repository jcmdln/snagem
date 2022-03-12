# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Update(BaseModel):
    categories: Optional[list[str]]
    description: Optional[str]
    subtitles: Optional[list[str]]
    tags: Optional[list[str]]
    title: Optional[str]


class Create(Update):
    source_url: str


class Delete(BaseModel):
    uuid: str


class Base(Create, Delete, Update):
    date_created: datetime
    date_updated: datetime
    duration: int
    views: int

    class Config:
        orm_mode = True


__all__: list[str] = ["Base", "Create", "Delete", "Update"]
