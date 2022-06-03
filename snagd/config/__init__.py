# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

backend_url: str | None = getenv("SNAGEM_BACKEND_URL")
broker_url: str | None = getenv("SNAGEM_BROKER_URL")
database_url: str = getenv("SNAGEM_DATABASE_URL", "sqlite:///snagd.db")
task_timeout: int = 30

__all__: list[str] = ["backend_url", "broker_url", "database_url", "task_timeout"]
