from fastapi import APIRouter

from snagem import task

router = APIRouter()


@router.get("/health")
def health_api() -> str:
    return "ok"


@router.get("/health/worker")
def health_worker() -> str:
    health_task = task.health.worker.delay()
    result: str = health_task.get()
    return result


__all__: list[str] = ["router"]
