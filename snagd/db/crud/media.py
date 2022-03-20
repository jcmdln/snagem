# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Type

from snagd.db import model
from snagd.db.crud import Base
from snagd.db.schema.media import MediaCreate, MediaDelete, MediaRead, MediaUpdate


class Media(Base[model.Media, MediaCreate, MediaDelete, MediaRead, MediaUpdate]):
    def __init__(self, model: Type[model.Media] = model.Media) -> None:
        self.model = model


__all__: list[str] = ["Media"]
