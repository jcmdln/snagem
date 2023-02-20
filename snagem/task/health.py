from snagem.task.session import celery


@celery.task
def worker() -> str:
    return "ok"


__all__: list[str] = ["worker"]
