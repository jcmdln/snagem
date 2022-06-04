# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from os import getenv

backend_url: str | None = getenv("SNAGEM_BACKEND_URL")
broker_url: str | None = getenv("SNAGEM_BROKER_URL")
database_url: str = getenv("SNAGEM_DATABASE_URL", "sqlite:///snagd.db")
task_time_limit: int = int(getenv("SNAGEM_TASK_TIME_LIMIT", 300))

print("Settings")
print("--------")
print(f"backend_url    : {backend_url}")
print(f"broker_url     : {broker_url}")
print(f"database_url   : {database_url}")
print(f"task_time_limit: {task_time_limit}")
print("")

__all__: list[str] = ["backend_url", "broker_url", "database_url", "task_time_limit"]
