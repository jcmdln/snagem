`snagem` provides a simple way to track, retrieve and manage content so it may
be enjoyed on your schedule.

# Using

## Quickstart

```sh
pipx install .
snagem server
```

## Docker-Compose

```sh
docker-compose build api &&
docker-compose up --detach &&
docker-compose logs -f
```

# Contributing

```
echo "GET http://127.0.0.1:5150/v1/health" |
vegeta attack -duration=30s -rate=250/1s |
vegeta encode > results.json &&
vegeta report results.*
```
