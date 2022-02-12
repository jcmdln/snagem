# SPDX-License-Identifier: AGPL-3.0-or-later

from typing import List

from fastapi import APIRouter

from snagd.api.v1.endpoints import router as endpoints_router

router = APIRouter()
router.include_router(endpoints_router)

__all__: List[str] = ["router"]
