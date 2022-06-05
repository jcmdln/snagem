# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Iterator

from alembic import command
from alembic import config as alembic_config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from snagd.config import config as snagd_config

database_args: dict = {}

if "sqlite" in snagd_config.SQLALCHEMY_URL.lower():
    database_args = {"check_same_thread": False}

engine: Engine = create_engine(snagd_config.SQLALCHEMY_URL, connect_args=database_args)
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def upgrade() -> None:
    cfg = alembic_config.Config("alembic.ini")
    command.upgrade(cfg, revision="head")


__all__: list[str] = ["Base", "SessionLocal", "engine", "get", "upgrade"]
