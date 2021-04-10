#!/usr/bin/python

##################################################
## Model from ingredient controller
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

import json


class ModelControllerIngredient:

    def __init__(self, id, name, calories):
        self.id = id
        self.name = name
        self.calories = calories

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
