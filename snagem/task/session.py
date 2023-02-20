from celery import Celery

from snagem import settings

celery = Celery(backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL)

celery.conf.update(task_always_eager=not settings.CELERY_BROKER_URL)
celery.conf.update(task_time_limit=settings.CELERY_TASK_TIME_LIMIT)

__all__: list[str] = ["celery"]
