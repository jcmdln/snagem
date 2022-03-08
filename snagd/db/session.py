# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

db_scheme: str = getenv("SNAGEM_DB_SCHEME", "sqlite")
db_user: str = getenv("SNAGEM_DB_USER", "")
db_pass: str = getenv("SNAGEM_DB_PASS", "")
db_host: str = getenv("SNAGEM_DB_HOST", "")
db_port: str = getenv("SNAGEM_DB_PORT", "")
db_path: str = getenv("SNAGEM_DB_PATH", "")

if "sqlite" in db_scheme.lower():
    db_args: dict = {"connect_args": {"check_same_thread": False}, "poolclass": StaticPool}
    db_url = f"{db_scheme}://{db_path}"
else:
    db_args = {}
    db_url = f"{db_scheme}://{db_user}:{db_pass}@{db_host}:{db_port}"

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(db_url, connect_args=db_args)
)


class Base(DeclarativeMeta):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


__all__: list[str] = ["Base", "SessionLocal", "db_url"]
