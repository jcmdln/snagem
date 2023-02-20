from fastapi import APIRouter

from snagem.route.v1.health import router as health_router
from snagem.route.v1.media import router as media_router

router = APIRouter()

router.include_router(health_router)
router.include_router(media_router)

__all__: list[str] = ["router"]
