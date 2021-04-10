#!/usr/bin/python

##################################################
## Storage model to store receipts
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################


# SqlAlchemy
from sqlalchemy import Column, ForeignKey, Table, Integer, String
from sqlalchemy.orm import relationship

# Modules
from app.persistance.model.base import Base

receipt_ingredient_table = Table(
    'receipt_ingredient', Base.metadata,
    Column('receipt_id', Integer, ForeignKey('receipt.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
)


class Receipt(Base):
    """Receipt with different ingredients"""
    __tablename__ = 'receipt'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(512), nullable=True)
    ingredients = relationship('Ingredient', secondary=receipt_ingredient_table)

    def __init__(self, name, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = ingredients
