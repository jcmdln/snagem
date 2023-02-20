from snagem.db.crud.base import Base
from snagem.db.model import media as model
from snagem.db.schema.media import Create, Delete, Read, Update


class Media(Base[model.Media, Create, Delete, Read, Update]):
    def __init__(self, model: type[model.Media] = model.Media) -> None:
        self.model = model


__all__: list[str] = ["Media"]
