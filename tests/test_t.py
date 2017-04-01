import pytest
from t import app


@pytest.fixture
def client(request):
    c = app.test_client()
    return c


def test_index(client):
    index = client.get("/", follow_redirects=True)
    assert index.status_code == 418
