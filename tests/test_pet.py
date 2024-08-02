import pytest
import requests


def test_get_pet(base_url, created_pet):
    """Проверяем, что GET запрос на получение питомца возвращает правильные данные"""
    pet_id = created_pet["id"]
    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_get_pet_not_found(base_url):
    """Проверяем, что GET запрос на несуществующего питомца возвращает 404"""
    pet_id = 999999
    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 404


def test_create_pet(base_url, new_pet):
    """Проверяем, что POST запрос на создание нового питомца работает корректно"""
    response = requests.post(f"{base_url}/pet", json=new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == new_pet["name"]


def test_create_pet_with_invalid_data(base_url):
    """Проверяем, что POST запрос с некорректными данными возвращает ошибку"""
    invalid_pet = {"id": "invalid_id", "name": 12345}
    response = requests.post(f"{base_url}/pet", json=invalid_pet)
    assert response.status_code in [400, 405, 500]  # Ожидаем любую ошибку, включая 500


def test_update_pet(base_url, created_pet, updated_pet):
    """Проверяем, что PUT запрос на обновление данных питомца работает корректно"""
    updated_pet["id"] = created_pet["id"]
    response = requests.put(f"{base_url}/pet", json=updated_pet)
    assert response.status_code == 200
    assert response.json()["name"] == updated_pet["name"]
    assert response.json()["status"] == updated_pet["status"]


def test_update_non_existent_pet(base_url):
    """Проверяем, что PUT запрос на несуществующего питомца работает корректно (ожидаем 200)"""
    updated_pet = {
        "id": 999999,
        "name": "NonExistentPet",
        "photoUrls": [],
        "tags": [],
        "status": "sold"
    }
    response = requests.put(f"{base_url}/pet", json=updated_pet)
    assert response.status_code in [200, 404]  # Ожидаем 200 или 404


def test_delete_pet(base_url, created_pet):
    """Проверяем, что DELETE запрос на удаление питомца работает корректно"""
    pet_id = created_pet["id"]
    response = requests.delete(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 200

    # Проверяем, что питомца больше нет
    response = requests.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 404


def test_delete_non_existent_pet(base_url):
    """Проверяем, что DELETE запрос на несуществующего питомца работает корректно (ожидаем 200)"""
    pet_id = 999999
    response = requests.delete(f"{base_url}/pet/{pet_id}")
    assert response.status_code in [200, 404]  # Ожидаем 200 или 404
