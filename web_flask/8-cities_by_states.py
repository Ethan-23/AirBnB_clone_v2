#!/usr/bin/python3
"""Flask states"""

from models import storage
from models.state import State
from models.state import City
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def hello_city():
    """gets states for html"""
    state = storage.all(State).values()
    city = storage.all(City).values()
    return render_template('8-cities_by_states.html', states=state,
                           cities=city)


@app.teardown_appcontext
def close_world(self):
    """close"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
