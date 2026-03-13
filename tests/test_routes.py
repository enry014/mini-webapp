import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_log(client):
    response = client.post("/add-log", data={"log": "test entry"})
    assert response.status_code == 200
    assert b"test entry" in response.data