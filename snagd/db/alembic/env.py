# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from logging.config import fileConfig
from typing import Optional

from alembic import context
from sqlalchemy import engine_from_config, pool

from snagd.config import config as snagd_config
from snagd.db import session

config = context.config
metadata = session.Base.metadata

if config.config_file_name:
    fileConfig(fname=config.config_file_name)
else:
    fileConfig(fname="alembic.ini")


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    opts = {"paramstyle": "named"}
    context.configure(url=url, target_metadata=metadata, literal_binds=True, dialect_opts=opts)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    cfg: Optional[dict] = config.get_section(config.config_ini_section)
    if not cfg:
        return

    cfg["sqlalchemy.url"] = snagd_config.SQLALCHEMY_URL
    connectable = engine_from_config(cfg, prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
