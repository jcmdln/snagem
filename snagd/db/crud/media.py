# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from typing import Type

from snagd.db import model
from snagd.db.crud import Base
from snagd.db.schema import media


class Media(Base[model.Media, media.Create, media.Delete, media.Update]):
    def __init__(self, model: Type[model.Media] = model.Media):
        self.model = model


__all__: list[str] = ["Media"]
