# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snagd.api.v2.media import router as media_router

router = APIRouter(tags=["v2"])
router.include_router(media_router)

app = FastAPI(docs_url="/", redoc_url=None, title="Snagem v2")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)
app.include_router(media_router)

__all__: list[str] = ["app", "router"]
