from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_login_valid_user():
    login_data = {
        "username": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post("/login/access-token", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_user():
    login_data = {
        "username": "nonexistent@example.com",
        "password": "invalidpassword"
    }
    response = client.post("/login/access-token", data=login_data)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Incorrect email/password"

def test_register_new_user():
    user_data = {
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
        "password": "newuserpassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["first_name"] == "New"
    assert data["last_name"] == "User"

def test_register_existing_user():
    user_data = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "The user with this email already exists in the system"

def test_validate_token():
    valid_token = "valid_token_here"
    response = client.get(f"/validate_token/{valid_token}")
    assert response.status_code == 200
    data = response.json()

