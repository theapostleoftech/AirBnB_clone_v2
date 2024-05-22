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


@app.route('/cities_by_states', strict_slashes=False)
def list_states_cities_route():
    """List all the states and its cities to the client"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def terminate_db(db):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
