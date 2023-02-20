from datetime import datetime
from uuid import uuid4 as new_uuid

from sqlalchemy import Column, DateTime, String

from snagem.db import session


class Setting(session.Base):
    __tablename__ = "setting"

    uuid = Column(String, default=new_uuid, nullable=False, primary_key=True, unique=True)

    name = Column(String, nullable=False, unique=True)
    value = Column(String, nullable=False)

    date_updated = Column(DateTime, default=datetime.now, nullable=False)


__all__: list[str] = ["Setting"]
