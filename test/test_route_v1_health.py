from fastapi.testclient import TestClient
from snagem.route.router import app

client: TestClient = TestClient(app)


def test_route_v1_health() -> None:
    response = client.get("/v1/health")
    assert response.status_code == 200


def test_route_v1_health_worker() -> None:
    response = client.get("/v1/health/worker")
    assert response.status_code == 200
