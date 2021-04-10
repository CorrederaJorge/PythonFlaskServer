#!/usr/bin/python

##################################################
## Contorller in charge of communicate to storage controoler
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# Injector
from injector import inject

# Modules
from app.persistance.receipt_storage import ReceiptStorage


class ReceiptController:
    @inject
    def __init__(self, receipt_storage: ReceiptStorage):
        self.receipt_storage = receipt_storage

    def set_receipt(self, receipt):
        self.receipt_storage.set_receipt(receipt)

    def get_receipt(self, receipt_id):
        return self.receipt_storage.get_receipt(receipt_id)

    def update_receipt(self, receipt):
        self.receipt_storage.update_receipt(receipt)

    def delete_receipt(self, receipt_id):
        self.receipt_storage.delete_receipt(receipt_id)

    def set_ingredient(self, ingredient):
        self.receipt_storage.set_ingredient(ingredient)

    def get_ingredient(self, ingredient_id):
        return self.receipt_storage.get_ingredient(ingredient_id)

    def update_ingredient(self, ingredient):
        self.receipt_storage.update_ingredient(ingredient)

    def delete_ingredient(self, ingredient_id):
        self.receipt_storage.delete_ingredient(ingredient_id)

    def get_receipt_calories(self, receipt_id):
        receipt = self.receipt_storage.get_receipt(receipt_id)
        return receipt.get_calories()
