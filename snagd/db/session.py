# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

db_args: dict = {}
db_proto: str = getenv("DB_PROTO", "sqlite")
db_uri: str = ""

if "sqlite" in db_proto.lower():
    db_args = {"connect_args": {"check_same_thread": False}, "poolclass": StaticPool}
    db_uri = "sqlite:///snagd.db"
elif "postgres" in db_proto.lower():
    db_uri = "postgres+psycopg://{}:{}@{}:{}".format(
        getenv("DB_USER"), getenv("DB_PASS"), getenv("DB_HOST"), getenv("DB_PORT")
    )
else:
    print("error: Unknown database backend! Exiting...")
    exit(1)

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(db_uri, connect_args=db_args)
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


__all__: list[str] = ["Base", "SessionLocal"]
