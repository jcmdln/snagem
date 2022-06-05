# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from importlib.metadata import version as pkg_version
from logging.config import fileConfig
from sys import exit

import click

from uvicorn import run as uvicorn_run

from snagd.api import app
from snagd.config import config
from snagd.db import session
from snagd.task.session import celery


@click.command(name="snagd", context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--host", default=config.UVICORN_HOST, type=str)
@click.option("--log-level", default=config.SNAGEM_LOG_LEVEL, type=str)
@click.option("--port", default=config.UVICORN_PORT, type=int)
@click.version_option(pkg_version("snagem"), "--version")
def snagd_server(host: str, log_level: str, port: int) -> None:
    log_level.lower()

    if port < 1 or port > 65535:
        print("error: invalid port {}! Must be an int between 1-65535".format(port))

    session.upgrade()
    fileConfig(fname="alembic.ini", disable_existing_loggers=False)
    uvicorn_run(app=app, host=host, port=port, log_config=None, log_level=log_level.lower())
    exit(0)


@click.command(name="snagd-worker", context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(pkg_version("snagem"), "--version")
def snagd_worker() -> None:
    celery.start(argv=["--app=snagd.task.session", "worker", "--concurrency=1", "--loglevel=info", "--task-events"])
    exit(0)


if __name__ == "__main__":
    snagd_server()
