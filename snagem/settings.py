from os import cpu_count, getenv

LOG_FILE: str | None = getenv("LOG_FILE")
LOG_LEVEL: str = getenv("LOG_LEVEL", "DEBUG").upper()

CELERY_BROKER_URL: str | None = getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND: str | None = getenv("CELERY_RESULT_BACKEND")
CELERY_TASK_TIME_LIMIT: int = int(getenv("CELERY_TASK_TIME_LIMIT", 300))
CELERYD_AUTOSCALER: str = getenv("CELERYD_AUTOSCALER", f"2,{cpu_count()}")
SQLALCHEMY_URL: str = getenv("SQLALCHEMY_URL", "sqlite:////tmp/snagem.db")
UVICORN_PORT = int(getenv("UVICORN_PORT", "5150"))
UVICORN_URL: str = getenv("UVICORN_URL", "127.0.0.1")

__all__: list[str] = [
    "LOG_FILE",
    "LOG_LEVEL",
    "CELERY_BROKER_URL",
    "CELERY_RESULT_BACKEND",
    "CELERY_TASK_TIME_LIMIT",
    "CELERYD_AUTOSCALER",
    "SQLALCHEMY_URL",
    "UVICORN_PORT",
    "UVICORN_URL",
]
