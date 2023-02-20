from snagem.db.crud import media as crud
from snagem.db.model import media as model
from snagem.db.schema import media as schema
from snagem.db.session import session
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
) -> schema.Media | dict:
    obj: schema.Create = schema.Create(
        uuid=uuid,
        categories=categories,
        description=description,
        tags=tags,
        title=title,
        source_url=source_url,
    )
    query: model.Media | None = crud.Media().create(db=session(), obj=obj)
    result: schema.Media | dict = schema.Media.from_orm(query).dict()
    return result


@celery.task
def delete(uuid: str) -> schema.Media | dict:
    obj: schema.Delete = schema.Delete(uuid=uuid)
    query: model.Media | None = crud.Media().delete(db=session(), obj=obj)
    result: schema.Media | dict = schema.Media.from_orm(query).dict()
    return result


@celery.task
def read(uuid: str) -> schema.Media | dict:
    query: model.Media | None = crud.Media().read(db=session(), uuid=uuid)
    result: schema.Media | dict = schema.Media.from_orm(query)
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
) -> list[schema.Media | dict]:
    obj: schema.Read = schema.Read(
        uuid=uuid,
        source_url=source_url,
        categories=categories,
        description=description,
        subtitles=subtitles,
        tags=tags,
        title=title,
    )

    result: list[schema.Media | dict] = []
    for item in crud.Media().search(db=session(), obj=obj):
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
) -> schema.Media | dict:
    obj: schema.Update = schema.Update(
        source_url=source_url,
        categories=categories,
        description=description,
        tags=tags,
        title=title,
    )
    query: model.Media | None = crud.Media().update(db=session(), obj=obj, uuid=uuid)
    result: schema.Media | dict = schema.Media.from_orm(query).dict()
    return result


__all__: list[str] = ["create", "delete", "read", "search", "update"]
