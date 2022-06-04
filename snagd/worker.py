# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from celery import Celery

from snagd import config

celery = Celery(name="worker", backend=config.backend_url, broker=config.broker_url)

celery.conf.update(kwargs={"task_time_limit": config.task_time_limit})

__all__: list[str] = ["celery"]
