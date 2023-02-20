import logging
from logging import Logger
from pathlib import Path

from snagem import settings


def logger() -> Logger:
    log: Logger = logging.getLogger("snagem")

    if settings.LOG_FILE:
        try:
            with Path(settings.LOG_FILE).open("a") as fd:
                fd.close()
        except FileNotFoundError as e:
            log.warning(e)
            settings.LOG_FILE = None

    log.propagate = False
    log.setLevel(settings.LOG_LEVEL)

    if not log.hasHandlers():
        formatter = logging.Formatter(
            "%(asctime)s %(name)s: %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        stream_h = logging.StreamHandler()
        stream_h.setFormatter(formatter)
        log.addHandler(stream_h)

        if settings.LOG_FILE:
            file_h = logging.FileHandler(settings.LOG_FILE)
            file_h.setFormatter(formatter)
            log.addHandler(file_h)

    return log


__all__: list[str] = ["logger", "Logger"]
