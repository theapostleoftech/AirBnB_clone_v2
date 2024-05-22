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


@app.route('/states', strict_slashes=False)
def states_route():
    """List all the states and its cities to the client"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id_route(id):
    """List all the states if the id exist to the client"""
    flag = 0
    states = None
    states_all = storage.all(State).values()
    for state in states_all:
        if id in state.id:
            flag = 1
            states = state
            break
    return render_template('9-states.html', states=states, flag=flag)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_route():
    """List all the states and its cities in dinamic content"""
    states = storage.all(State).values()
    am = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=am)


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Print the home page in dinamic content"""
    st = storage.all(State).values()
    am = storage.all(Amenity).values()
    pl = storage.all(Place).values()
    return render_template('100-hbnb.html', states=st, amenities=am, places=pl)


@app.teardown_appcontext
def terminate_db(db):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
