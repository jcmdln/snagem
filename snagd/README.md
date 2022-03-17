Testing
---
* https://docs.celeryproject.org/en/stable/userguide/testing.html

### Local
```sh
$ sudo dnf --refresh -y install libpq-devel git poetry python3-devel sqlite-devel
$ poetry install
$ poetry run tox
```

### Container
```sh
$ sudo dnf --refresh -y install podman
$ podman build . --tag jcmdln/snagem:devel --target devel
$ podman run -it jcmdln/snagem:devel
```


Alembic
---
```sh
$ poetry run alembic revision --autogenerate -m "example"
$ poetry run alembic upgrade head
```
