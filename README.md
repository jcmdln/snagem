`snagem` provides a simple way to track, retrieve and manage content so it may be enjoyed on your
schedule.

See the following for subcomponent documentation:
* [snag](./snag/README.md)
* [snagd](./snagd/README.md)


Quickstart
---
This section outlines how to quickly run snagem using Fedora 35 as an example.

### Local
```sh
$ sudo dnf --refresh -y install git libpq-devel python3-devel sqlite-devel
# FIXME: poetry>=1.2,<2 once released
$ pip install --user poetry==1.2.0b1
$ poetry install --only default
$ poetry run snagd
2022-03-26 02:24:05 INFO: alembic.runtime.migration: Context impl SQLiteImpl.
2022-03-26 02:24:05 INFO: alembic.runtime.migration: Will assume non-transactional DDL.
2022-03-26 02:24:05 INFO: uvicorn.error: Started server process [548350]
2022-03-26 02:24:05 INFO: uvicorn.error: Waiting for application startup.
2022-03-26 02:24:05 INFO: uvicorn.error: Application startup complete.
2022-03-26 02:24:05 INFO: uvicorn.error: Uvicorn running on http://127.0.0.1:5050 (Press CTRL+C to quit)
```

### Container
```sh
$ sudo dnf --refresh -y install podman
$ podman build . --tag jcmdln/snagem:release --target release
$ podman run -it jcmdln/snagem:release
2022-03-26 02:24:05 INFO: alembic.runtime.migration: Context impl SQLiteImpl.
2022-03-26 02:24:05 INFO: alembic.runtime.migration: Will assume non-transactional DDL.
2022-03-26 02:24:05 INFO: uvicorn.error: Started server process [548350]
2022-03-26 02:24:05 INFO: uvicorn.error: Waiting for application startup.
2022-03-26 02:24:05 INFO: uvicorn.error: Application startup complete.
2022-03-26 02:24:05 INFO: uvicorn.error: Uvicorn running on http://127.0.0.1:5050 (Press CTRL+C to quit)
```

Contributing
---
### Getting Started
* https://python-poetry.org/docs
* https://fastapi.tiangolo.com
    * https://pydantic-docs.helpmanual.io
    * https://docs.sqlalchemy.org
        * https://alembic.sqlalchemy.org
    * https://docs.celeryq.dev
        * https://docs.celeryq.dev/projects/kombu


### Testing
This section outlines how to test snagem using Fedora 35 as an example.

#### Local
```sh
$ sudo dnf --refresh -y install git libpq-devel python3-devel sqlite-devel
# FIXME: poetry>=1.2,<2 once released
$ pip install --user poetry==1.2.0b1
$ poetry install
$ poetry run tox
```

#### Container
```sh
$ sudo dnf --refresh -y install podman
$ podman build . --tag jcmdln/snagem:devel --target devel
$ podman run -it jcmdln/snagem:devel
```
