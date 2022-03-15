# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

from celery import Celery

from snagd.task import media

backend_url: str | None = getenv("BACKEND_URL")
broker_url: str = getenv("BROKER_URL", "ampq://guest@localhost/")
celery = Celery("snager", backend=backend_url, broker=broker_url)

__all__: list[str] = ["celery", "media"]
