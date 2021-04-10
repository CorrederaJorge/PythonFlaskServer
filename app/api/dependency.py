#!/usr/bin/python

##################################################
## Dependency injector for Flask
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

# Flask
from flask_injector import request

# Modules
from app.controller.receipt_controller import ReceiptController
from app.persistance.receipt_storage import ReceiptStorage


def configure(binder):
    binder.bind(ReceiptStorage, to=ReceiptStorage, scope=request)
    binder.bind(ReceiptController, to=ReceiptController, scope=request)
