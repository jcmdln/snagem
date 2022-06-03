# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from celery import Celery

from snagd.config import backend_url, broker_url

celery = Celery(name="worker", backend=backend_url, broker=broker_url)

__all__: list[str] = ["celery"]
