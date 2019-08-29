#!/usr/bin/python3
"""
Starts a Flask web application with the following conditions

- listens on 0.0.0.0, port 5000
- routes
  - /:         display “Hello HBNB!”
  - /hbnb:     display “HBNB”
  - /c/<text>: display 'C ' followed by <text>
                 - replaces underscores _ with spaces
"""

from flask import Flask

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
    """ Displays 'C' followed by the value of the `text` variable"""
    text = text.replace("_", " ")
    return 'C ' + text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
