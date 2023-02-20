from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        orm_mode: bool = True


__all__: list[str] = ["Base"]
