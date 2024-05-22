#!/usr/bin/python3
"""
Start a web application to listen on port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Hello route listening on 0.0.0.0 port 5000
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    hbnb route listening on 0.0.0.0 port 5000
    """
    return 'HBNB'


if '__name' == '__main__':
    app.run(host='0.0.0.0', port=5000)
