from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from snagem.db import session


class Media(session.Base):
    __tablename__ = "media"

    uuid = Column(String, nullable=False, primary_key=True, unique=True)

    source_url = Column(String, nullable=False)
    title = Column(String, default="title")
    description = Column(String)
    duration = Column(Integer, default=0, nullable=False)
    subtitles = Column(String)

    categories = Column(String)
    tags = Column(String)
    views = Column(Integer, default=0, nullable=False)

    date_created = Column(DateTime, default=datetime.now, nullable=False)
    date_updated = Column(DateTime, default=datetime.now, nullable=False)


__all__: list[str] = ["Media"]
