##################################################
## Readme file
##################################################
## No license
##################################################
## Author: Jorge Corredera
## Version: 0.1.0
## Status: development
##################################################

To install it you need to use virtual environment and all the libraries contained in requirements.txt. 

For that:

Create and activate a virtual environment:

$ python3.9 -m venv env
$ source env/bin/activate
(env)$

(env)$ pip install -r requirements.txt


If you want to run test
(env)$ python -m pytest

If you want to run flask
(env)$ FLASK_APP=project/app.py python -m flask run

As an alternative you can use PyCharm and install two new debug configurations like show in flask_pychar.png and pytest_pycharm.png
