`snagem` provides a simple way to track, retrieve, and manage content from sites
supported by [youtube-dl](https://github.com/ytdl-org/youtube-dl) so it may be
enjoyed on your schedule.

See the following for subcomponent documentation:
* [snagctl](./snagctl/README.md)
* [snagd](./snagd/README.md)


Quickstart
---
This section outlines how to quickly run Snagem

### Local
```sh
$ sudo dnf --refresh -y install libpq-devel git poetry python3-devel sqlite-devel
$ poetry install --no-dev
$ poetry run snagd
INFO:     Started server process [$PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:5050 (Press CTRL+C to quit)
```

### Container
```sh
$ sudo dnf --refresh -y install podman
$ podman build . --tag jcmdln/snagem:release --target release
$ podman run -it jcmdln/snagem:release
INFO:     Started server process [$PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:5050 (Press CTRL+C to quit)
```


Contributing
---
### Getting Started
* https://fastapi.tiangolo.com/tutorial/
* https://docs.sqlalchemy.org/en/20/tutorial/index.html
* https://pydantic-docs.helpmanual.io/
* https://alembic.sqlalchemy.org/en/latest/tutorial.html
* https://docs.celeryproject.org/en/stable/getting-started/index.html
* https://docs.celeryproject.org/projects/kombu/en/stable/introduction.html
