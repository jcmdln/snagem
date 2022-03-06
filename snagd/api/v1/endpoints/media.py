# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/media")
def media() -> dict:
    return {"": ""}


@router.get("/media/{uuid}")
def media_info(uuid: str) -> dict:
    return {"uuid": uuid}


@router.post("/media/add")
def media_add(source_url: str) -> dict:
    return {
        "url": source_url,
    }


@router.delete("/media/remove")
def media_remove(uuid: str) -> dict:
    return {
        "uuid": uuid,
    }


@router.put("/media/update")
def media_update(uuid: str) -> dict:
    return {
        "uuid": uuid,
    }
