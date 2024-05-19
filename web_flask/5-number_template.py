#!/usr/bin/python3
"""
A script that starts a Flask web application
listening on 0.0.0.0:5000
"""

from flask import Flask, render_template

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
def hello_c_route(text):
    """
    This functions displays C followed by
    the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python_route(text):
    """
    This function displays Python followed by
    the value of the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def hello_number_route(n):
    """
    This function displays n is a number
    if n is an integer
    """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        return '4ot Found', 404
    


@app.route('/number_template/<n>', strict_slashes=False)
def hello_number_template_route(n):
    """
    This function displays a HTML page
    if n is an integer
    """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        return '4ot Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
