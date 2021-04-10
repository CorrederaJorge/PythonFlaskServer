#!/usr/bin/python

##################################################
## Controller exceptions
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Email: 
## Status: development
##################################################

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ElementNotPresent(Error):
    """Raised when theres is no element in storage system"""
    pass


class UnknownErrorInStorageSystem(Error):
    """Raised when theres is an unknown error - Check Logs"""
    pass
