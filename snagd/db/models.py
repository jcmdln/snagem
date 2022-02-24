# SPDX-License-Identifier: AGPL-3.0-or-later


from sqlalchemy import Column, DateTime, Integer, String

from snagd.db.session import Base


class Media(Base):  # type: ignore
    """Media model."""

    categories: Column[String]
    date_created: Column[DateTime]
    date_updated: Column[DateTime]
    description: Column[String]
    duration: Column[Integer]
    source_url: Column[String]
    subtitles: Column[String]
    tags: Column[String]
    title: Column[String]
    uuid: Column[String]
    views: Column[Integer]
