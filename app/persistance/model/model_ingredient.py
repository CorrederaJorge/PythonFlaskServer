#!/usr/bin/python

##################################################
## Storage model to store ingredients
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# SqlAlchemy
from sqlalchemy import Column, Integer, String

# Modules
from app.persistance.model.base import Base


class Ingredient(Base):
    """Dish Ingredients"""
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    calories = Column(Integer)

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
