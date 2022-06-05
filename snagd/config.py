# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv


class SnagdConfig:
    SNAGEM_LOG_LEVEL: str = "debug"
    CELERY_BROKER_URL: str | None = None
    CELERY_RESULT_BACKEND: str | None = None
    CELERY_TASK_TIME_LIMIT: int = 300
    SQLALCHEMY_URL: str = "sqlite:////tmp/snagd.db"
    UVICORN_HOST: str = "127.0.0.1"
    UVICORN_PORT: int = 5150

    def init_env(self) -> None:
        """
        Load values from the environment.

        `init_env` has a higher precedence than `init_file`, though is superceeded by cli flags.
        """
        self.SNAGEM_LOG_LEVEL = getenv("SNAGEM_LOG_LEVEL", self.SNAGEM_LOG_LEVEL).lower()
        self.CELERY_BROKER_URL = getenv("CELERY_BROKER_URL", self.CELERY_BROKER_URL)
        self.CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND", self.CELERY_RESULT_BACKEND)
        self.CELERY_TASK_TIME_LIMIT = int(getenv("CELERY_TASK_TIME_LIMIT", self.CELERY_TASK_TIME_LIMIT))
        self.SQLALCHEMY_URL = getenv("SQLALCHEMY_URL", self.SQLALCHEMY_URL)
        self.UVICORN_HOST = getenv("UVICORN_URL", self.UVICORN_HOST)
        self.UVICORN_PORT = int(getenv("UVICORN_PORT", self.UVICORN_PORT))

    def init_file(self) -> None:
        """
        Load values from the configuration file.

        `init_file` has the lowest variable precedence and is superceeded by env vars, and ultimately cli flags.
        """
        pass


config: SnagdConfig = SnagdConfig()

# CLI flags > env vars > config file
config.init_file()
config.init_env()

__all__: list[str] = ["config"]
