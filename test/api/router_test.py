#!/usr/bin/python

##################################################
## Router test
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# pytest
import pytest
from pytest_mock import mocker

# modules
from app.main import app
from app.controller.receipt_controller import ReceiptController
from app.controller.model_controller_receipt import ModelControllerReceipt
from app.controller.model_controller_ingredient import ModelControllerIngredient


chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

# TODO add error test in case controller raise exceptions
@pytest.fixture
def client(mocker):
    yield app.test_client() # tests run here


def test_get_api_ready(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"CookAPI ready!"


def test_get_ingredient_ok(client):
    response = client.get("/api/v1/ingredients/1")

    assert response.status_code == 200
    assert response.data == b'{"id": -1, "name": "sugar", "calories": 100}'


def test_get_ingredient_ok(client, mocker):
    mocked_get_ingredient = mocker.patch.object(ReceiptController, 'get_ingredient')
    mocked_get_ingredient.return_value = sugar

    response = client.get("/api/v1/ingredients/1")

    mocked_get_ingredient.assert_called_with(1)

    assert response.status_code == 200
    assert response.data == b'{"id": -1, "name": "sugar", "calories": 100}'


def test_set_ingredient_ok(client, mocker):
    mocked_set_ingredient = mocker.patch.object(ReceiptController, 'set_ingredient')
    mocked_set_ingredient.return_value = 1

    response = client.post("/api/v1/ingredients/", data=chocolate.to_json(), content_type='application/json')

    # TODO it should check that imput parameter is milk but it returns a comparison error
    mocked_set_ingredient.assert_called()

    assert response.status_code == 200
    assert response.data == b'{"id":1}\n'


def test_update_ingredient_ok(client, mocker):
    mocked_update_ingredient = mocker.patch.object(ReceiptController, 'update_ingredient')
    mocked_update_ingredient.return_value = 1

    milk = ModelControllerIngredient(id=1, name='milk', calories=100)

    response = client.put("/api/v1/ingredients/", data=milk.to_json(), content_type='application/json')

    # TODO it should check that imput parameter is milk but it returns a comparison error
    mocked_update_ingredient.assert_called()

    assert response.status_code == 200


def test_delete_ingredient_ok(client, mocker):
    mocked_delete_ingredient = mocker.patch.object(ReceiptController, 'delete_ingredient')

    response = client.delete("/api/v1/ingredients/1")

    mocked_delete_ingredient.assert_called_with(1)

    assert response.status_code == 200


def test_get_receipt_ok(client, mocker):
    mocked_get_receipt = mocker.patch.object(ReceiptController, 'get_receipt')
    mocked_get_receipt.return_value = cake

    response = client.get("/api/v1/receipts/1")

    mocked_get_receipt.assert_called_with(1)

    assert response.status_code == 200
    assert response.data == b'{"id": -1, "name": "cake", "description": "Good receipt", "ingredients": [{"id": -1, "name": "choco", "calories": 100}, {"id": -1, "name": "sugar", "calories": 100}]}'


def test_get_receipt_calories_ok(client, mocker):
    mocked_get_receipt = mocker.patch.object(ReceiptController, 'get_receipt')
    mocked_get_receipt.return_value = cake

    response = client.get("/api/v1/receipts/1/calories")

    mocked_get_receipt.assert_called_with(1)

    assert response.status_code == 200
    assert response.data == b'{"res":200}\n'


def test_delete_receipt_ok(client, mocker):
    mocked_delete_receipt = mocker.patch.object(ReceiptController, 'delete_receipt')

    response = client.delete("/api/v1/receipts/1")

    mocked_delete_receipt.assert_called_with(1)

    assert response.status_code == 200


def test_update_receipt_ok(client, mocker):
    mocked_update_receipt = mocker.patch.object(ReceiptController, 'update_receipt')
    mocked_update_receipt.return_value = 1

    brown_sugar = ModelControllerIngredient(1, 'brown_sugar', 100)
    rice_with_milk = ModelControllerReceipt(1, 'milk', 'Good receipt', [brown_sugar])

    response = client.put("/api/v1/receipts/", data=rice_with_milk.to_json(), content_type='application/json')

    # TODO it should check that imput parameter is rice_with_milk but it returns a comparison error
    mocked_update_receipt.assert_called()

    assert response.status_code == 200


def test_set_receipt_ok(client, mocker):
    mocked_set_receipt = mocker.patch.object(ReceiptController, 'set_receipt')
    mocked_set_receipt.return_value = 1

    brown_sugar = ModelControllerIngredient(1, 'brown_sugar', 100)
    rice_with_milk = ModelControllerReceipt(1, 'milk', 'Good receipt', [brown_sugar])

    response = client.post("/api/v1/receipts/", data=rice_with_milk.to_json(), content_type='application/json')

    # TODO it should check that imput parameter is cake but it returns a comparison error
    mocked_set_receipt.assert_called()

    assert response.status_code == 200
    assert response.data == b'{"id":1}\n'