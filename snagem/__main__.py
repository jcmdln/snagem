from importlib.metadata import version as pkg_version

import click

from snagem import settings
from snagem.logger import Logger, logger


@click.group(name="snagem", context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=pkg_version("snagem"))
def cli() -> None:
    pass


@click.command(name="server")
@click.option("--log-level", default=settings.LOG_LEVEL, type=str)
@click.option("--host", default=settings.UVICORN_URL, type=str)
@click.option("--port", default=settings.UVICORN_PORT, type=int)
def server(log_level: str, host: str, port: int) -> None:
    log: Logger = logger()
    log.info("Server")

    if port < 1 or port > 65535:
        log.error("invalid port:", port)

    from snagem.db import session

    session.upgrade()

    from logging.config import fileConfig

    fileConfig(fname="alembic.ini", disable_existing_loggers=False)

    from uvicorn import run as uvicorn_run

    from snagem.route.router import app

    uvicorn_run(app=app, host=host, port=port, log_config=None, log_level=log_level.lower())


@click.command(name="worker")
def worker() -> None:
    log: Logger = logger()
    log.info("Worker")

    from snagem.task.session import celery

    celery.start(
        argv=[
            "--app=snagem.task.session",
            "worker",
            f"--autoscale={settings.CELERYD_AUTOSCALER}",
            f"--loglevel={settings.LOG_LEVEL}",
            "--task-events",
        ]
    )


cli.add_command(server)
cli.add_command(worker)


if __name__ == "__main__":
    cli()
