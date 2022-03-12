# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snagd.api import v1, v2

app = FastAPI(docs_url="/", redoc_url=None, title="Snagem")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)
app.include_router(v1.router, prefix="/v1", tags=["v1"])
app.include_router(v2.router, prefix="/v2", tags=["v2"])

app.mount("/v1", app=v1.app)
app.mount("/v2", app=v2.app)

__all__: list[str] = ["app"]
