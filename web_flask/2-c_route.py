#!/usr/bin/python3
"""
A script that starts a Flask web application
listening on 0.0.0.0:5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    This function displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb_route():
    """
    This functions displays HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c_route():
    """
    This functions displays C followed by
    the value of the text variable
    """
    return "C" + '<text>'