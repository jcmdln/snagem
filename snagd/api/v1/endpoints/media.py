# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Form

router = APIRouter()


@router.get("/media")
def media_list() -> dict:
    return {"": ""}


@router.post("/media/add")
def media_add(media_name: Optional[str] = Form(None), media_url: str = Form(...)) -> dict:
    return {
        "name": media_name,
        "url": media_url,
    }
