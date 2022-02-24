# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Media(BaseModel):
    """Media schema."""

    source_url: str
    date_created: datetime
    duration: int

    categories: list[str] | None
    date_updated: datetime | None
    description: str | None
    subtitles: list[str] | None
    tags: list[str] | None
    title: str | None
    uuid: str | None
    views: int | None


class MediaCreate(BaseModel):
    """MediaCreate schema."""

    source_url: str

    categories: list[str] | None
    description: str | None
    duration: int | None
    tags: list[str] | None
    title: str | None


class MediaDelete(BaseModel):
    """MediaDelete schema."""

    uuid: str


class MediaUpdate(BaseModel):
    """MediaUpdate schema."""

    categories: list[str] | None
    description: str | None
    duration: int | None
    source_url: str | None
    subtitles: list[str] | None
    tags: list[str] | None
    title: str | None
    views: int | None
