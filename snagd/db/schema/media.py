# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Create(BaseModel):
    source_url: str

    categories: Optional[list[str]]
    description: Optional[str]
    tags: Optional[list[str]]
    title: Optional[str]


class Delete(BaseModel):
    uuid: UUID


class Update(BaseModel):
    categories: Optional[list[str]]
    description: Optional[str]
    source_url: Optional[str]
    subtitles: Optional[list[str]]
    tags: Optional[list[str]]
    title: Optional[str]


class Base(Create, Delete, Update):
    date_created: datetime
    date_updated: datetime
    duration: int
    source_url: str
    views: int


__all__: list[str] = ["Base", "Create", "Delete", "Update"]
