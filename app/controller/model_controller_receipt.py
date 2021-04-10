#!/usr/bin/python

##################################################
## Model from receipt controller
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

import json


class ModelControllerReceipt:

    def __init__(self, id, name, description, ingredients):
        self.id = id
        self.name = name
        self.description = description
        self.ingredients = ingredients

    def get_calories(self):
        calories = 0
        for ingredient in self.ingredients:
            calories += ingredient.calories

        return calories

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)