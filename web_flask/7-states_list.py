#!/usr/bin/python3
"""Flask states"""

from models import storage
from flask import Flask
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello_state():
    """gets states for html"""
    state = storage.all(State)
    return render_template('7-states_list.html', states=state)


@app.teardown_appcontext
def close_world():
    """close"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
