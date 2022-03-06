# SPDX-License-Identifier: AGPL-3.0-or-later

from importlib.metadata import version as pkg_version
from sys import exit

import click

from uvicorn import run as uvicorn_run

from snagd import app


@click.command(name="snagd")
@click.option("--log-level", default="debug", type=str)
@click.option("--host", default="127.0.0.1", type=str)
@click.option("--port", default=5050, type=int)
@click.option("--version", default=False, is_flag=True, type=bool)
def main(host: str, log_level: str, port: int, version: bool) -> None:
    if version:
        print("snagd v{}".format(pkg_version("snagem")))
        exit(0)

    if port < 1 or port > 65535:
        print("error: invalid port {}! Must be an int between 1-65535".format(port))

    uvicorn_run(app=app, host=host, port=port, log_level=log_level)

    exit(0)


if __name__ == "__main__":
    main()
