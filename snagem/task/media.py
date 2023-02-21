from snagem.db import session
from snagem.db.crud import media as crud
from snagem.db.model import media as model
from snagem.db.schema import media as schema
from snagem.task.session import celery


@celery.task
def create(
    *,
    uuid: str,
    source_url: str | None,
    categories: list[str] | None,
    description: str | None,
    tags: list[str] | None,
    title: str | None,
) -> dict:
    query: model.Media | None = crud.Media().create(
        db=session.get(),
        obj=schema.Create(
            uuid=uuid,
            categories=categories,
            description=description,
            tags=tags,
            title=title,
            source_url=source_url,
        ),
    )
    result: dict = schema.Media.from_orm(query).dict()
    return result


@celery.task
def delete(uuid: str) -> dict:
    query: model.Media | None = crud.Media().delete(db=session.get(), obj=schema.Delete(uuid=uuid))
    result: dict = schema.Media.from_orm(query).dict()
    return result


@celery.task
def read(uuid: str) -> dict:
    query: model.Media | None = crud.Media().read(db=session.get(), uuid=uuid)
    result: dict = schema.Media.from_orm(query).dict()
    return result


@celery.task
def search(
    *,
    uuid: str | None,
    source_url: str | None,
    categories: list[str] | None,
    description: str | None,
    subtitles: list[str] | None,
    tags: list[str] | None,
    title: str | None,
) -> list[dict]:
    obj: schema.Read = schema.Read(
        uuid=uuid,
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )

    result: list[dict] = []
    for item in crud.Media().search(db=session.get(), obj=obj):
        result.append(schema.Media.from_orm(item).dict())

    return result


@celery.task
def update(
    *,
    uuid: str,
    source_url: str | None,
    categories: list[str] | None,
    description: str | None,
    tags: list[str] | None,
    title: str | None,
) -> dict:
    query: model.Media | None = crud.Media().update(
        db=session.get(),
        obj=schema.Update(
            source_url=source_url,
            categories=categories,
            description=description,
            tags=tags,
            title=title,
        ),
        uuid=uuid,
    )
    result: dict = schema.Media.from_orm(query).dict()
    return result


__all__: list[str] = ["create", "delete", "read", "search", "update"]
