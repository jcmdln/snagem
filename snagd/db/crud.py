# SPDX-License-Identifier: AGPL-3.0-or-later

import uuid

from typing import Generic, TypeVar

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from snagd.db import models, schemas

MediaSchemaType = TypeVar("MediaSchemaType", bound=schemas.Media)
MediaCreateSchemaType = TypeVar("MediaCreateSchemaType", bound=schemas.MediaCreate)
MediaDeleteSchemaType = TypeVar("MediaDeleteSchemaType", bound=schemas.MediaDelete)
MediaUpdateSchemaType = TypeVar("MediaUpdateSchemaType", bound=schemas.MediaUpdate)


class Media(
    Generic[MediaSchemaType, MediaCreateSchemaType, MediaDeleteSchemaType, MediaUpdateSchemaType]
):
    """Media CRUD."""

    def __init__(self, db: Session, model: MediaSchemaType) -> None:
        self.db_session = db
        self.model = model

    def create(self, media: schemas.MediaCreate) -> MediaSchemaType:
        """Create Media."""

        new_media = models.Media(
            categories=media.categories,
            description=media.description,
            duration=media.duration,
            source_url=media.source_url,
            tags=media.tags,
            title=media.title,
            uuid=uuid.UUID(),
        )

        self.db_session.add(new_media)
        self.db_session.commit()
        self.db_session.refresh(new_media)

        return new_media

    def delete(self, media: schemas.MediaDelete) -> MediaSchemaType:
        """Delete media."""

        del_media: models.Media | None = (
            self.db_session.query(self.model).filter(models.Media.uuid == media.uuid).first()
        )

        if not del_media:
            raise HTTPException(status_code=404, detail="media not found: {}".format(media))

        self.db_session.delete(del_media)
        self.db_session.commit()

        return del_media

    def read(self, media: schemas.Media) -> models.Media:
        """Read media."""

        pass

    def update(self, media: schemas.MediaUpdate) -> MediaSchemaType:
        """Update media."""

        obj_data = jsonable_encoder(self.model)

        if isinstance(media, dict):
            update_data = media
        else:
            update_data = media.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(self.model, field, update_data[field])

        self.db_session.add(self.model)
        self.db_session.commit()
        self.db_session.refresh(self.model)

        return self.model
