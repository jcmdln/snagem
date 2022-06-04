NOTE: This project doesn't do much yet! Sorry!

`snagem` provides a simple way to track, retrieve and manage content so it may be enjoyed on your
schedule.

See the following for subcomponent documentation:

-   [snag](./snag/README.md)
-   [snagd](./snagd/README.md)

## Quickstart

This section outlines how to quickly run snagem using Fedora 36 as an example.

### Locally

If you want to run snagem quickly and minimally, running `snagd` only requires sqlite:

```sh
$ virtualenv .venv
$ source .venv/bin/activate
(.venv) $ pip install .
(.venv) $ snagd
2022-06-03 18:37:32 INFO: alembic.runtime.migration: Context impl SQLiteImpl.
2022-06-03 18:37:32 INFO: alembic.runtime.migration: Will assume non-transactional DDL.
2022-06-03 18:37:32 INFO: alembic.runtime.migration: Running upgrade  -> 8cc1e0b83c3b
2022-06-03 18:37:32 INFO: uvicorn.error: Started server process [568860]
2022-06-03 18:37:32 INFO: uvicorn.error: Waiting for application startup.
2022-06-03 18:37:32 INFO: uvicorn.error: Application startup complete.
2022-06-03 18:37:32 INFO: uvicorn.error: Uvicorn running on http://127.0.0.1:5150 (Press CTRL+C to quit)
```

### Container

Snagem doesn't require being run in a container but it's really convenient for seeing how a
polylith deployment works. This makes use of Postgres, Rabbit and Redis while providing an example
of how Snagem might be packaged into more complex deployment systems which are outside the scope
of this project.

```sh
$ sudo dnf -y install docker-compose podman
$ systemctl --user enable --now podman.sock
$ export DOCKER_HOST="unix:///run/user/$UID/podman/podman.sock"
$ docker-compose up
```

## Contributing

### Getting Started

-   https://python-poetry.org/docs
-   https://fastapi.tiangolo.com
    -   https://pydantic-docs.helpmanual.io
    -   https://docs.sqlalchemy.org
        -   https://alembic.sqlalchemy.org
    -   https://docs.celeryq.dev
        -   https://docs.celeryq.dev/projects/kombu

```sh
# Install Poetry
# TODO: poetry>=1.2,<2 once released
$ curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@ac49097

# Install Snagem dependencies
$ poetry install

# Run Tox
$ poetry run tox
```
