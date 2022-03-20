# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

import uuid


def new_uuid() -> str:
    return uuid.uuid4().__str__()


__all__: list[str] = ["new_uuid"]
