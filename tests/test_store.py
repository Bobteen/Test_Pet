import pytest
import requests


def test_get_inventory(base_url):
    """Проверяем, что GET запрос на получение инвентаря возвращает статус 200"""
    response = requests.get(f"{base_url}/store/inventory")
    assert response.status_code == 200


def test_create_order(base_url):
    """Проверяем, что POST запрос на создание заказа возвращает статус 200 и правильные данные"""
    new_order = {
        "id": 1,
        "petId": 12345,
        "quantity": 1,
        "shipDate": "2024-08-01T12:34:56.789Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{base_url}/store/order", json=new_order)
    assert response.status_code == 200
    assert response.json()["id"] == new_order["id"]


def test_get_order_by_id(base_url):
    """Проверяем, что GET запрос на получение заказа по ID возвращает статус 200 и правильные данные"""
    order_id = 1
    response = requests.get(f"{base_url}/store/order/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id


def test_delete_order(base_url):
    """Проверяем, что DELETE запрос на удаление заказа возвращает статус 200"""
    order_id = 1
    response = requests.delete(f"{base_url}/store/order/{order_id}")
    assert response.status_code == 200


def test_get_order_not_found(base_url):
    """Проверяем, что GET запрос на несуществующий заказ возвращает статус 404"""
    order_id = 999999
    response = requests.get(f"{base_url}/store/order/{order_id}")
    assert response.status_code == 404
