#!/usr/bin/python

##################################################
## Routes all the API calls - It is based on Flask
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

import json

from app import config

# Flask
from flask import Flask, Response, request, jsonify
from flask_injector import FlaskInjector
from injector import inject

# Modules
from app.api.dependency import configure
from app.controller.receipt_controller import ReceiptController
from app.controller.model_controller_ingredient import ModelControllerIngredient
from app.api.json_utils import json2obj

app = Flask(__name__)
app.config.from_object(config.Config)


@app.route("/")
def ready():
    return "CookAPI ready!"


@inject
@app.route('/api/v1/receipts/<int:index>', methods=['GET'])
def get_receipt(controller: ReceiptController, index):
    """
    Get receipts based on receipt id
    :param controller:
    :param index:
    :return: Return response with JSON object found
    """
    try:
        receipt = controller.get_receipt(index)
        response = receipt.to_json()
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return response


@inject
@app.route('/api/v1/receipts/', methods=['POST'])
def set_receipt(controller: ReceiptController):
    """
    Post a receipt
    :param controller:
    :return: receipt id
    """
    try:
        content = json.dumps(request.json)
        receipt = json2obj(content)
        receipt_id = controller.set_receipt(receipt)
        response = {'id': receipt_id}
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return jsonify(response)


@inject
@app.route('/api/v1/receipts/', methods=['PUT'])
def update_receipt(controller: ReceiptController):
    """
    Update a receipt
    :param controller:
    :return:
    """
    try:
        content = json.dumps(request.json)
        receipt = json2obj(content)
        controller.update_receipt(receipt)
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return Response("Ok", status=200, mimetype='application/json')


@inject
@app.route('/api/v1/receipts/<int:index>', methods=['DELETE'])
def delete_receipt(controller: ReceiptController, index):
    """
    Delete receipt
    :param controller:
    :param index: receipt id to be deleted
    :return: status message
    """
    try:
        controller.delete_receipt(index)
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return Response("Ok", status=200, mimetype='application/json')


@inject
@app.route('/api/v1/ingredients/<int:index>', methods=['GET'])
def get_ingredient(controller: ReceiptController, index):
    """
    Get ingredient
    :param controller:
    :param index: ingredient id to be obtained
    :return: Return response with JSON object found
    """
    try:
        receipt = controller.get_ingredient(index)
        response = receipt.to_json()
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return response


@inject
@app.route('/api/v1/ingredients/', methods=['POST'])
def set_ingredient(controller: ReceiptController):
    """
    Post ingredient from json data
    :param controller:
    :return: status message
    """
    try:
        content = json.dumps(request.json)
        ingredient = json.loads(content, object_hook=lambda d: ModelControllerIngredient(**d))
        ingredient_id = controller.set_ingredient(ingredient)
        response = {'id': ingredient_id}
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return jsonify(response)


@inject
@app.route('/api/v1/ingredients/', methods=['PUT'])
def update_ingredient(controller: ReceiptController):
    """
    Update ingredient data
    :param controller:
    :return: status message
    """
    try:
        content = json.dumps(request.json)
        ingredient = json.loads(content, object_hook=lambda d: ModelControllerIngredient(**d))
        controller.update_ingredient(ingredient)
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return Response("Ok", status=200, mimetype='application/json')


@inject
@app.route('/api/v1/ingredients/<int:index>', methods=['DELETE'])
def delete_ingredient(controller: ReceiptController, index):
    """
    Delete ingredient
    :param controller:
    :param index: ingredient id to be deleted
    :return: status message
    """
    try:
        controller.delete_ingredient(index)
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return Response("Ok", status=200, mimetype='application/json')


@inject
@app.route('/api/v1/receipts/<int:index>/calories', methods=['GET'])
def get_receipt_calories(controller: ReceiptController, index):
    """
    Get calories from receipt
    :param controller:
    :param index: receipt id to get calories from
    :return: res containing calories per 100 g
    """
    try:
        receipt = controller.get_receipt(index)
        calories = receipt.get_calories()
        response = {'res': calories}
    except Exception as e:
        print(e)
        return Response("Error", status=500, mimetype='application/json')

    return response


# Setup Flask Injector, this has to happen AFTER routes are added
FlaskInjector(app=app, modules=[configure])
