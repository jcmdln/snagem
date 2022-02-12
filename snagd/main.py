# SPDX-License-Identifier: AGPL-3.0-or-later

import logging

from importlib.metadata import version

import click
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snagd.api import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(router)


@click.command(name="snagd")
@click.option("--log-level", default="debug")
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=5050)
def main(host: str, log_level: str, port: int) -> None:
    log = logging.getLogger("snagd")

    log.info("snagd v{}".format(version("snagem")))

    # TODO: Allow cli args -> Env vars -> default precedence
    log.debug("log_level: {}".format(log_level))
    log.debug("host: {}".format(host))
    log.debug("port: {}".format(port))

    log.info("Starting uvicorn...")
    uvicorn.run(app=app, host=host, port=port, log_level=log_level)


if __name__ == "__main__":
    main()
