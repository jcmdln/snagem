# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter

from snagd.api.v1 import router as v1_router

router = APIRouter()

router.include_router(v1_router, prefix="/v1", tags=["v1"])


__all__: list[str] = ["router"]
