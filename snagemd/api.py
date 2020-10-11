from typing import Any, Dict, List, Optional

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class Media(BaseModel):  # type: ignore
    duration: int
    encoding: str
    language: str
    name: str
    size: float
    source: str
    tags: List[str]


class Playlist(BaseModel):  # type: ignore
    name: str
    tags: List[str]


class Settings(BaseModel):  # type: ignore
    domains_allow: Optional[List[str]]
    domains_deny: Optional[List[str]]
    encoding_audio: Optional[Dict[Any, Any]]
    encoding_video: Optional[Dict[Any, Any]]
    ratelimit: Optional[int]
    quotas: Optional[int]


class Sources(BaseModel):  # type: ignore
    name: Optional[str]
    url: str


@app.get("/")
def media_list() -> Dict[Any, Any]:
    return {"Hello": "World"}


@app.get("/{media_id}")
def media_info(media_id: int, q: Optional[str] = None) -> Dict[Any, Any]:
    return {"media_id": media_id, "q": q}


@app.put("/{media_id}")
def media_update(media_id: int, media: Media) -> Dict[Any, Any]:
    return {"media_name": media.name, "media_id": media_id}


@app.get("/sources")
def sources_list() -> Dict[Any, Any]:
    return {"": ""}


@app.post("/sources/add")
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


@app.delete("/sources/remove")
def sources_remove(source_id: int, source: Sources) -> Dict[Any, Any]:
    return {"source_name": source.name, "source_id": source_id}
