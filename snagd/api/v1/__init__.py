from typing import List

from fastapi import APIRouter

from snagd.api.v1.endpoints import sources_router

api_router = APIRouter()
api_router.include_router(sources_router, prefix="/sources", tags=["sources"])

__all__: List[str] = ["api_router"]
