#!/usr/bin/python3
"""
Starts a Flask web application with the following conditions

- listens on 0.0.0.0, port 5000
- routes
  - /:                    display “Hello HBNB!”
  - /hbnb:                display “HBNB”
  - /c/<text>:            display 'C ' followed by <text>
                            - replaces underscores _ with spaces
  - /python/(<text>):     display 'Python ', followed by <text>
                            - replaces underscores _ with spaces
  - /number/<n>:          display "n is a number" only if n is an integer
  - /number_template/<n>: display a HTML page only if n is an integer
                            - H1 tag: “Number: n” inside the tag BODY
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays 'C ' followed by the value of the `text` variable """
    text = text.replace("_", " ")
    return 'C ' + text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ Displays 'Python ' followed by the value of the `text` variable """
    text = text.replace("_", " ")
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ Displays 'n is a number' only if n is an integer """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
