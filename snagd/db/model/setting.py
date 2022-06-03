# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, String

from snagd.db import session
from snagd.util import new_uuid


class Setting(session.Base):
    __tablename__ = "setting"

    uuid = Column(String, default=new_uuid, nullable=False, primary_key=True, unique=True)
    name = Column(String, nullable=False, unique=True)
    date_updated = Column(DateTime, default=datetime.now, nullable=False)


__all__: list[str] = ["Setting"]
