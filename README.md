`snagem` provides a simple way to track, retrieve and manage content so it may be enjoyed on your
schedule.

See the following for subcomponent documentation:
* [snagctl](./snagctl/README.md)
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
