#!/usr/bin/python3
"""
Starts a Flask web application with the following conditions

- listens on 0.0.0.0, port 5000
- routes
  - /hbnb_filters: shows hbnb filters page
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ shows hbnb filters page  """
    return render_template("10-hbnb_filters.html",
                           states=storage.all("State").values(),
                           amenities=storage.all("Amenity").values())

@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
