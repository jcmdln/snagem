# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from fastapi import APIRouter, Form

router = APIRouter()


@router.get("/sources")
def sources_list() -> dict:
    return {"": ""}


@router.post("/sources/add")
def sources_add(
    source_name: str | None = Form(None), source_url: str = Form(...)
) -> dict:
    """
    Add the `source_url` of a supported media type to track and retrieve.

    The `source_url` will be referenced on further additions to prevent
    duplicates and ensure that should our copy of the target be marked as
    missing, it can be retrieved. If the source_url no longer resolves then
    any associated media files will be orphaned and excluded from checks.
    """
    return {
        "name": source_name,
        "url": source_url,
    }
