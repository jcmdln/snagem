# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime
from typing import Optional

from snagd.db.schema.base import Base


class MediaUpdate(Base):
    categories: Optional[list[str]]
    description: Optional[str]
    subtitles: Optional[list[str]]
    tags: Optional[list[str]]
    title: Optional[str]


class MediaCreate(MediaUpdate):
    source_url: str


class MediaDelete(Base):
    uuid: str


class MediaRead(MediaUpdate):
    source_url: Optional[str]
    uuid: Optional[str]


class Media(MediaCreate, MediaDelete, MediaUpdate):
    date_created: datetime
    date_updated: datetime
    duration: int
    views: int


__all__: list[str] = ["Media", "MediaCreate", "MediaDelete", "MediaRead", "MediaUpdate"]
