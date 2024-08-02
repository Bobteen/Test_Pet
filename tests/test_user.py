import requests
import pytest


def test_create_user(base_url, new_user):
    """Проверяем, что POST запрос на создание пользователя возвращает статус 200 и правильные данные"""
    response = requests.post(f"{base_url}/user", json=new_user)
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_get_user_by_username(base_url, created_user):
    """Проверяем, что GET запрос на получение пользователя по имени возвращает статус 200 и правильные данные"""
    username = created_user["username"]
    response = requests.get(f"{base_url}/user/{username}")
    assert response.status_code == 200
    assert response.json()["username"] == username


def test_update_user(base_url, created_user):
    """Проверяем, что PUT запрос на обновление данных пользователя возвращает статус 200 и правильные данные"""
    updated_user = {
        "id": created_user["id"],
        "username": created_user["username"],
        "firstName": "UpdatedTest",
        "lastName": "User",
        "email": "updateduser@example.com",
        "password": "newpassword123",
        "phone": "0987654321",
        "userStatus": 1
    }
    response = requests.put(f"{base_url}/user/{created_user['username']}", json=updated_user)
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_delete_user(base_url, created_user):
    """Проверяем, что DELETE запрос на удаление пользователя возвращает статус 200"""
    username = created_user["username"]
    response = requests.delete(f"{base_url}/user/{username}")
    assert response.status_code == 200


def test_login_user(base_url, created_user):
    """Проверяем, что GET запрос на логин пользователя возвращает статус 200 и включает правильное сообщение"""
    username = created_user["username"]
    password = created_user["password"]
    response = requests.get(f"{base_url}/user/login", params={"username": username, "password": password})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["code"] == 200
    assert json_response["message"].startswith("logged in user session:")
    assert json_response["type"] == "unknown"


def test_logout_user(base_url):
    """Проверяем, что GET запрос на логаут пользователя возвращает статус 200"""
    response = requests.get(f"{base_url}/user/logout")
    assert response.status_code == 200
