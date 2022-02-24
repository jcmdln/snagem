# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Generator

from snagd.db import models, schemas
from snagd.db.session import SessionLocal
from snagd.utils import Log, Logger

log: Logger = Log("database")


def get_db() -> Generator:
    """Universal function to create a database session."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


__all__: list[str] = ["Base", "SessionLocal", "get_db", "models", "schemas"]
