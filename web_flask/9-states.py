#!/usr/bin/python3
"""Flask states"""

from models import storage
from models.state import State
from models.city import City
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def hello_state():
    """gets states for html"""
    state = storage.all(State)
    return render_template('9-states.html', states=state, switch=0)


@app.route('/states/<id>', strict_slashes=False)
def hello_state_id(id=None):
    """gets states for html"""
    state = storage.all(State)
    city = storage.all(City)
    name = None
    for i in state.values():
        if i.id == id:
            name = i.name
    return render_template('9-states.html', states=state, cities=city,
                           ids=id, switch=1, name=name)


@app.teardown_appcontext
def close_world(self):
    """close"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
