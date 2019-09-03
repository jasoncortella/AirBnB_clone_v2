#!/usr/bin/python3
"""
Starts a Flask web application with the following conditions

- listens on 0.0.0.0, port 5000
- routes
  - /cities_by_states: lists state objects in dbstorage and associated cities
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays state objects in dbstorage and associated cities """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
