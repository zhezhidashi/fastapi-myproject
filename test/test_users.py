from main import app
from fastapi.testclient import TestClient
from routers import users

client = TestClient(app)

# 获取token
def get_token():
    response = client.post(
        "/login/",
        json = {
            "username": "zzh01",
            "passwd": "zzh01"
        }
    )
    return response.json().get("access_token")

def test_get_users():
    response = client.get("/users/get-users?token=" + get_token())
    assert response.status_code == 200

def test_add_user():
    response = client.post(
        "/users/add-user?token=" + get_token(),
        json = {
            "username": "user-test",
            "passwd": "user-test"
        }
    )
    assert response.status_code == 200

def test_delete_user():
    response = client.post(
        "/users/delete-user?token=" + get_token(),
        json = {
            "username": "user-test"
        }
    )
    assert response.status_code == 200