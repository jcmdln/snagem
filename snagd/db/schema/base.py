# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        orm_mode: bool = True


__all__: list[str] = ["Base"]
