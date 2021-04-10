#!/usr/bin/python

##################################################
## Test receipt controller
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# Pytest
from pytest_mock import mocker

# Modules
from app.controller.receipt_controller import ReceiptController
from app.controller.model_controller_receipt import ModelControllerReceipt
from app.controller.model_controller_ingredient import ModelControllerIngredient
from app.persistance.receipt_storage import ReceiptStorage


def test_set_ingredient_call_storage_properly(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'set_ingredient')

    receipt_controller = ReceiptController(ReceiptStorage())

    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    receipt_controller.set_ingredient(sugar)

    mocked_internal_func.assert_called_with(sugar)


def test_get_ingredient_call_storage_properly(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'get_ingredient')
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    mocked_internal_func.return_value = sugar
    receipt_controller = ReceiptController(ReceiptStorage())

    sugar_id = 1
    read_ingredient = receipt_controller.get_ingredient(sugar_id)

    mocked_internal_func.assert_called_with(sugar_id)
    assert sugar == read_ingredient


def test_delete_ingredient(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'delete_ingredient')

    receipt_controller = ReceiptController(ReceiptStorage())

    sugar_id = 1
    receipt_controller.delete_ingredient(sugar_id)

    mocked_internal_func.assert_called_with(sugar_id)


def test_update_ingredient(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'update_ingredient')

    receipt_controller = ReceiptController(ReceiptStorage())

    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    receipt_controller.update_ingredient(sugar)

    mocked_internal_func.assert_called_with(sugar)


def test_set_receipt_call_storage_properly(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'set_receipt')

    receipt_controller = ReceiptController(ReceiptStorage())
    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)

    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    receipt_controller.set_receipt(cake)

    mocked_internal_func.assert_called_with(cake)


def test_get_receipt(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'get_receipt')

    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    mocked_internal_func.return_value = cake

    receipt_controller = ReceiptController(ReceiptStorage())

    sugar_id = 1
    read_receipt = receipt_controller.get_receipt(sugar_id)

    mocked_internal_func.assert_called_with(sugar_id)
    assert cake == read_receipt


def test_delete_receipt(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'delete_receipt')

    receipt_controller = ReceiptController(ReceiptStorage())

    receipt_id = 1
    receipt_controller.delete_receipt(receipt_id)

    mocked_internal_func.assert_called_with(receipt_id)


def test_update_receipt(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'update_receipt')

    receipt_controller = ReceiptController(ReceiptStorage())

    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    receipt_controller.update_receipt(sugar)

    mocked_internal_func.assert_called_with(sugar)


def test_get_receipt_calories(mocker):
    mocked_internal_func = mocker.patch.object(ReceiptStorage, 'get_receipt')

    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)
    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    mocked_internal_func.return_value = cake

    receipt_controller = ReceiptController(ReceiptStorage())

    cake_receipt_id = 1
    calories = receipt_controller.get_receipt_calories(cake_receipt_id)

    mocked_internal_func.assert_called_with(cake_receipt_id)

    assert calories == cake.get_calories()

