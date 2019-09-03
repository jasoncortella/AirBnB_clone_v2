#!/usr/bin/python3
"""
Starts a Flask web application with the following conditions

- listens on 0.0.0.0, port 5000
- routes
  - /states:      lists state objects in dbstorage
  - /states/<id>: displays a state with specified id
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """ displays a state with specified id  """
    all_states = storage.all('State')
    if id:
        state_id = 'State.' + id
        if state_id in all_states:
            states = all_states[state_id]
        else:
            states = None
    else:
        states = all_states.values()
    return render_template('9-states.html',
                           states=states,
                           id=id)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
