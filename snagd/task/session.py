# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from celery import Celery

from snagd.config import config

celery = Celery(name="worker", backend=config.CELERY_RESULT_BACKEND, broker=config.CELERY_BROKER_URL)
celery.conf.update(kwargs={"task_time_limit": config.CELERY_TASK_TIME_LIMIT})

__all__: list[str] = ["celery"]
