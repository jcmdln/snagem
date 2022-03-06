# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Generator

from snagd.db import crud, model, schema, session


def get_db() -> Generator:
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()


__all__: list[str] = ["crud", "get_db", "model", "schema", "session"]
