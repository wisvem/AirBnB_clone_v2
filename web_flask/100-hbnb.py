#!/usr/bin/python3
""" Task 12 """
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template as render
from bisect import insort

app = Flask(__name__)
app.url_map.strict_slashes = False


all_states = storage.all(State)
all_amenities = storage.all(Amenity)
all_places = storage.all(Place)


@app.teardown_appcontext
def teardown(exception=None):
    """ Teardown """
    storage.close()


@app.route('/hbnb')
def hbnb():
    """Task 12 """
    return render('100-hbnb.html', all_states=all_states,
                  all_amenities=all_amenities, all_places=all_places)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
