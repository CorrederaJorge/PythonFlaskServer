#!/usr/bin/python

##################################################
## Test storage modules functions
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

from app.controller.model_controller_receipt import ModelControllerReceipt
from app.controller.model_controller_ingredient import ModelControllerIngredient


def test_calculate_receipt_calories():
    chocolate = ModelControllerIngredient(id=-1, name='choco', calories=100)
    sugar = ModelControllerIngredient(id=-1, name='sugar', calories=333)

    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [chocolate, sugar])

    assert cake.get_calories() == chocolate.calories + sugar.calories


def test_calculate_receipt_calories_return_zero_if_no_ingredients():
    cake = ModelControllerReceipt(-1, 'cake', 'Good receipt', [])

    assert cake.get_calories() == 0
