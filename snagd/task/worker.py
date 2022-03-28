# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

from celery import Celery

backend_url: str | None = getenv("BACKEND_URL")
broker_url: str | None = getenv("BROKER_URL")
celery = Celery("snagr", backend=backend_url, broker=broker_url)

__all__: list[str] = ["backend_url", "broker_url", "celery"]
