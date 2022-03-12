# SPDX-License-Identifier: AGPL-3.0-or-later

from sqlalchemy import Column, DateTime, Integer, String

from snagd.db import session


class Media(session.Base):
    __tablename__ = "media"

    uuid = Column(String, nullable=False, primary_key=True)
    categories = Column(String)
    date_created = Column(DateTime, nullable=False)
    date_updated = Column(DateTime, nullable=False)
    description = Column(String)
    duration = Column(Integer, nullable=False)
    source_url = Column(String, nullable=False)
    subtitles = Column(String)
    tags = Column(String)
    title = Column(String, nullable=False)
    views = Column(Integer, nullable=False)


__all__: list[str] = ["Media"]
