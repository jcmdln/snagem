# SPDX-License-Identifier: AGPL-3.0-or-later

from typing import List

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from snagd.api.v1 import router as v1_router

router = APIRouter()


@router.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


router.include_router(v1_router, prefix="/v1", tags=["v1"])

__all__: List[str] = ["router"]
