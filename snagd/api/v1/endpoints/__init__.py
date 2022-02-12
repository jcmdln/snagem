# SPDX-License-Identifier: AGPL-3.0-or-later

from typing import List

from fastapi import APIRouter

from snagd.api.v1.endpoints.sources import router as sources_router

router = APIRouter()
router.include_router(sources_router)

__all__: List[str] = ["router"]
