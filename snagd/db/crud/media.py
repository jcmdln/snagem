# SPDX-License-Identifier: AGPL-3.0-or-later

from snagd.db import model
from snagd.db.crud import Base
from snagd.db.schema import media


class Media(Base[model.Media, media.Create, media.Delete, media.Update]):
    pass


__all__: list[str] = ["Media"]
