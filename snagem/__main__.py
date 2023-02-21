from importlib.metadata import version as pkg_version
from logging.config import fileConfig

import click
from uvicorn import run as uvicorn_run

from snagem import settings
from snagem.db import session
from snagem.route.router import app
from snagem.task.session import celery


@click.group(name="snagem", context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=pkg_version("snagem"))
def cli() -> None:
    pass


@click.command(name="server")
@click.option("--log-level", default=settings.LOG_LEVEL, type=str)
@click.option("--host", default=settings.UVICORN_URL, type=str)
@click.option("--port", default=settings.UVICORN_PORT, type=int)
def server(log_level: str, host: str, port: int) -> None:
    session.upgrade()
    fileConfig(fname="alembic.ini", disable_existing_loggers=False)
    uvicorn_run(app=app, host=host, port=port, log_config=None, log_level=log_level.lower())


@click.command(name="worker")
def worker() -> None:
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
