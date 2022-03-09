# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snagd import api, db, snag
from snagd.api import router

app = FastAPI(docs_url="/", redoc_url=None, title="Snagem")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(router)

__all__: list[str] = ["api", "app", "db", "snag"]
