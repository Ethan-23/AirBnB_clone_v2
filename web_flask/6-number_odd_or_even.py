#!/usr/bin/python3
"""Flask setup"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Test command"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """HBNB"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """HBNB"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """HBNB"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_html(n):
    """HBNB"""
    return render_template('5-number.html', m=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_oddeven(n):
    """HBNB"""
    if n % 2 == 0:
        test = "{} is even".format(n)
    else:
        test = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', o=test)

if __name__ == "__main__":
    app.run(host="0.0.0.0")