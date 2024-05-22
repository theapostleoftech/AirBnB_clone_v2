#!/usr/bin/python3
"""
A script that lists all the states after
starting the web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states_route():
    """
    This function lists states in a HTML page
    sorted by name
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def terminate_db(exception):
    """
    This functin closes the database connection
    after each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
