snagd is the snagem server which provides an API that can be run with or without external
dependencies such as PostgreSQL, RabbitMQ, Redis.

This README briefly outlines how to test and contribute to snagd.


Testing
---
In this section, we'll demonstrate how to test snagd locally as well as in a container. Either
method can be used based on whichever is more convenient for you.

### Local
```sh
$ sudo dnf --refresh -y install git libpq-devel poetry python3-devel sqlite-devel
$ poetry install
$ poetry run tox
```

### Container
```sh
$ sudo dnf --refresh -y install podman
$ podman build . --tag jcmdln/snagem:devel --target devel
$ podman run -it jcmdln/snagem:devel
```


Contributing
---
### Getting Started
* https://python-poetry.org/docs
* https://fastapi.tiangolo.com/tutorial/
* https://docs.sqlalchemy.org/en/20/tutorial/index.html
* https://pydantic-docs.helpmanual.io/
* https://alembic.sqlalchemy.org/en/latest/tutorial.html
* https://docs.celeryproject.org/en/stable/getting-started/index.html
* https://docs.celeryproject.org/projects/kombu/en/stable/introduction.html
