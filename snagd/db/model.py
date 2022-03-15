# SPDX-License-Identifier: AGPL-3.0-or-later

import uuid

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from snagd.db import session


class Media(session.Base):
    __tablename__ = "media"

    uuid = Column(String, default=str(uuid.uuid4()), nullable=False, primary_key=True, unique=True)
    categories = Column(String)
    date_created = Column(DateTime, default=datetime.now, nullable=False)
    date_updated = Column(DateTime, default=datetime.now, nullable=False)
    description = Column(String)
    duration = Column(Integer, default=0, nullable=False)
    source_url = Column(String, nullable=False)
    subtitles = Column(String)
    tags = Column(String)
    title = Column(String, default="title", nullable=False)
    views = Column(Integer, default=0, nullable=False)


__all__: list[str] = ["Media"]
