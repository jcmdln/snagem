# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv
from typing import Iterator

from alembic import command, config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

db_args: dict = {}
db_url: str = getenv("DB_URL", "sqlite:///snagem.db")

if "sqlite" in db_url.lower():
    db_args = {"check_same_thread": False}

engine: Engine = create_engine(db_url, connect_args=db_args)
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


cfg = config.Config("alembic.ini")
command.upgrade(cfg, revision="head")


__all__: list[str] = ["Base", "SessionLocal", "db_url", "engine", "get"]
