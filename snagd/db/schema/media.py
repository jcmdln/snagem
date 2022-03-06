# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Media(BaseModel):
    categories: list[str]
    date_created: datetime
    date_updated: datetime
    description: str
    duration: int
    source_url: str
    subtitles: list[str]
    tags: list[str]
    title: str
    uuid: str
    views: int


class Create(BaseModel):
    source_url: str

    categories: Optional[list[str]]
    description: Optional[str]
    duration: Optional[int]
    tags: Optional[list[str]]
    title: Optional[str]


class Delete(BaseModel):
    uuid: UUID


class Update(BaseModel):
    categories: Optional[list[str]]
    description: Optional[str]
    duration: Optional[int]
    source_url: Optional[str]
    subtitles: Optional[list[str]]
    tags: Optional[list[str]]
    title: Optional[str]
    views: Optional[int]


__all__: list[str] = ["Media", "Create", "Delete", "Update"]
