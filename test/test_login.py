from main import app
from fastapi.testclient import TestClient
from routers import login

client = TestClient(app)

def test_login():
    response = client.post(
        "/login/",
        json = {
            "username": "zzh01",
            "passwd": "zzh01"
        }
    )
    assert response.status_code == 200
    assert response.json().get("access_token") != None