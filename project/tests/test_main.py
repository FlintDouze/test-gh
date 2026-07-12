from fastapi.testclient import TestClient

from project.main import app


client = TestClient(app)


def test_root_returns_hello_world() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_unknown_route_returns_404() -> None:
    response = client.get("/unknown")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_root_rejects_post_method() -> None:
    response = client.post("/")

    assert response.status_code == 405