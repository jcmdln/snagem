from typing import Any, Dict, Optional

from fastapi import APIRouter, Form

router = APIRouter()


@router.get("/")
def sources_list() -> Dict[Any, Any]:
    return {"": ""}


@router.post("/add")
def sources_add(
    source_name: Optional[str] = Form(None), source_url: str = Form(...)
) -> Dict[Any, Any]:
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
