#!/usr/bin/python

##################################################
## Test storage controller
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# Pytest
import pytest

# Modules
from app.persistance.receipt_storage import ReceiptStorage
from app.controller.model_controller_ingredient import ModelControllerIngredient
from app.controller.model_controller_receipt import ModelControllerReceipt
from app.controller.exceptions import ElementNotPresent


def test_set_ingredient():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    ingredient = ModelControllerIngredient(id=-1, name='salt', calories=100)
    ingredient_id = receipt_storage.set_ingredient(ingredient)

    read_ingredient = receipt_storage.get_ingredient(ingredient_id)

    assert read_ingredient.id == ingredient_id
    assert read_ingredient.name == ingredient.name
    assert read_ingredient.calories == ingredient.calories


def test_delete_ingredient():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    ingredient = ModelControllerIngredient(id=-1, name='salt', calories=100)
    ingredient_id = receipt_storage.set_ingredient(ingredient)
    receipt_storage.delete_ingredient(ingredient_id)
    read_ingredient = receipt_storage.get_ingredient(ingredient_id)
    assert read_ingredient is None


def test_update_ingredient():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    ingredient = ModelControllerIngredient(id=-1, name='salt', calories=100)
    ingredient_id = receipt_storage.set_ingredient(ingredient)

    update_ingredient = ModelControllerIngredient(id=ingredient_id, name='salt2', calories=200)
    receipt_storage.update_ingredient(update_ingredient)
    read_ingredient = receipt_storage.get_ingredient(ingredient_id)

    assert read_ingredient.id == update_ingredient.id
    assert read_ingredient.name == update_ingredient.name
    assert read_ingredient.calories == update_ingredient.calories


def test_update_not_stored_ingredient_raise_error():
    receipt_storage = ReceiptStorage()
    ingredient = ModelControllerIngredient(id=-1, name='salt', calories=100)

    with pytest.raises(ElementNotPresent):
        receipt_storage.update_ingredient(ingredient)


def test_set_receipt():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)

    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    cake_id = receipt_storage.set_receipt(cake)

    read_cake = receipt_storage.get_receipt(cake_id)

    assert read_cake.id == cake_id
    assert read_cake.name == cake.name
    assert read_cake.description == cake.description

    assert len(read_cake.ingredients) == 2
    assert read_cake.ingredients[0].name == cake.ingredients[0].name
    assert read_cake.ingredients[0].calories == cake.ingredients[0].calories

    assert read_cake.ingredients[1].name == cake.ingredients[1].name
    assert read_cake.ingredients[1].calories == cake.ingredients[1].calories


def test_set_receipt_with_empty_description():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    cake = ModelControllerReceipt(-1, 'cake', '', [])

    cake_id = receipt_storage.set_receipt(cake)

    read_cake = receipt_storage.get_receipt(cake_id)

    assert read_cake.description == cake.description


def test_delete_receipt():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)

    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    cake_id = receipt_storage.set_receipt(cake)

    read_cake = receipt_storage.delete_receipt(cake_id)
    assert read_cake is None


def test_update_receipt():
    receipt_storage = ReceiptStorage()
    receipt_storage.redo_db()

    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=100)

    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    cake_id = receipt_storage.set_receipt(cake)

    read_cake = receipt_storage.get_receipt(cake_id)
    read_cake.name = "updated_cake"
    read_cake.description = "Good receipt updated"

    read_cake.ingredients[0].name = "chocoUpdated"
    read_cake.ingredients[0].calories = 200

    receipt_storage.update_receipt(read_cake)

    updated_cake = receipt_storage.get_receipt(cake_id)

    assert read_cake.id == updated_cake.id
    assert read_cake.name == updated_cake.name
    assert read_cake.description == updated_cake.description

    assert len(read_cake.ingredients) == 2
    assert read_cake.ingredients[0].name == updated_cake.ingredients[0].name
    assert read_cake.ingredients[0].calories == updated_cake.ingredients[0].calories

    assert read_cake.ingredients[1].name == updated_cake.ingredients[1].name
    assert read_cake.ingredients[1].calories == updated_cake.ingredients[1].calories


def test_update_not_stored_receipt_raise_error():
    receipt_storage = ReceiptStorage()
    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [])

    with pytest.raises(ElementNotPresent):
        receipt_storage.update_receipt(cake)
