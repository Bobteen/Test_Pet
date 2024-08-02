import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API"""
    return BASE_URL


@pytest.fixture
def new_pet():
    return {
        "id": 12345,
        "name": "TestPet",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }


@pytest.fixture
def updated_pet(new_pet):
    pet = new_pet.copy()
    pet["name"] = "UpdatedTestPet"
    pet["status"] = "sold"
    return pet


@pytest.fixture
def created_pet(new_pet):
    """Создаем питомца перед тестом и удаляем его после"""
    response = requests.post(f"{BASE_URL}/pet", json=new_pet)
    assert response.status_code == 200
    yield new_pet
    requests.delete(f"{BASE_URL}/pet/{new_pet['id']}")


@pytest.fixture
def new_order():
    """Создаем новый заказ"""
    return {
        "id": 1,
        "petId": 12345,
        "quantity": 1,
        "shipDate": "2024-08-01T12:34:56.789Z",
        "status": "placed",
        "complete": True
    }


@pytest.fixture
def new_user():
    """Создаем нового пользователя"""
    return {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }


@pytest.fixture
def created_order(new_order):
    """Создаем заказ перед тестами и удаляем после"""
    response = requests.post(f"{BASE_URL}/store/order", json=new_order)
    yield new_order
    requests.delete(f"{BASE_URL}/store/order/{new_order['id']}")


@pytest.fixture
def created_user(new_user):
    """Создаем пользователя перед тестами и удаляем после"""
    response = requests.post(f"{BASE_URL}/user", json=new_user)
    yield new_user
    requests.delete(f"{BASE_URL}/user/{new_user['username']}")
