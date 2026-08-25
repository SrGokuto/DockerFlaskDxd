import pytest

from sample_app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_ejemplo_basico():
    assert 1 + 1 == 2


def test_home_ok(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido a mi aplicacion Flask" in response.get_data(as_text=True)