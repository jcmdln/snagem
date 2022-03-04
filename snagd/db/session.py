# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv
from typing import Optional

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from snagd.db import log

db_args: dict = {}
db_host: Optional[str] = getenv("DB_HOST")
db_name: Optional[str] = getenv("DB_NAME")
db_pass: Optional[str] = getenv("DB_PASS")
db_port: Optional[str] = getenv("DB_PORT", "5432")
db_proto: Optional[str] = getenv("DB_PROTO", "postgresql+psycopg")
db_user: Optional[str] = getenv("DB_USER")

if db_type and "postgres" in db_type.lower():
    if not db_host:
        log.error("Environment variable 'DB_HOST' unset!")
    if not db_name:
        log.error("Environment variable 'DB_NAME' unset!")
    if not db_pass:
        log.error("Environment variable 'DB_PASS' unset!")
    if not db_user:
        log.error("Environment variable 'DB_USER' unset!")
    if not db_host or not db_name or not db_pass or not db_user:
        log.error("Exiting...")
        exit(1)

    db_uri = "postgresql+psycopg://{}:{}@{}:{}".format(db_user, db_pass, db_host, db_port)
else:
    db_args = {"check_same_thread": False}
    db_uri = "sqlite:///snagd.db"

log.debug("'db_uri' is {}".format(db_uri))

engine: Engine = create_engine(db_uri, connect_args=db_args)
meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=meta)
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


__all__: list[str] = ["Base", "SessionLocal"]
