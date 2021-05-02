#!/usr/bin/python3
""" Task 10 """
from models import storage
from models.state import State
from flask import Flask, render_template as render


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters')
def hbnb():
    """Task 10 """
    render('100-hbnb.py')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
