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
(.venv) $ pip install git+https://github.com/python-poetry/poetry@51824fc
(.venv) $ poetry install --only main
(.venv) $ snagd
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
