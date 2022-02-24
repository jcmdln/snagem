# SPDX-License-Identifier: AGPL-3.0-or-later

import logging

from importlib.metadata import version
from sys import exit

import click

from uvicorn import run as uvicorn_run

from snagd import app


@click.command(name="snagd")
@click.option("--log-level", default="debug")
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=5050)
def main(host: str, log_level: str, port: int) -> None:
    """Snagd main."""

    log = logging.getLogger("snagd")

    log.info("snagd v{}".format(version("snagem")))

    # TODO: Allow cli args -> Env vars -> default precedence
    log.debug("log_level: {}".format(log_level))
    log.debug("host: {}".format(host))
    log.debug("port: {}".format(port))

    log.info("Starting uvicorn...")
    uvicorn_run(app=app, host=host, port=port, log_level=log_level)

    exit(0)


if __name__ == "__main__":
    main()
