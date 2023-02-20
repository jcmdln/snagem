from fastapi.testclient import TestClient

from snagem.route.router import app

client: TestClient = TestClient(app)


def _get_media_uuid() -> str:
    response = client.get("/v1/media")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    uuid: str = response.json()[0].get("uuid")
    return uuid


def test_route_v1_media_search() -> None:
    response = client.get("/v1/media")
    assert response.status_code == 200


def test_route_v1_media_create() -> None:
    response = client.post("/v1/media", params={"source_url": "domain.tld"})
    assert response.status_code == 200


def test_route_v1_media_read() -> None:
    response = client.get(f"/v1/media/{_get_media_uuid()}")
    assert response.status_code == 200


def test_route_v1_media_update() -> None:
    response = client.put(f"/v1/media/{_get_media_uuid()}")
    assert response.status_code == 200


def test_route_v1_media_delete() -> None:
    response = client.delete(f"/v1/media/{_get_media_uuid()}")
    assert response.status_code == 200
