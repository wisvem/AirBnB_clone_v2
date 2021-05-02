#!/usr/bin/python3
""" 10. State and states """
from flask import Flask, render_template as render
from models import storage
from models.state import State
from models.city import City
from bisect import insort

app = Flask(__name__)
app.url_map.strict_slashes = False
all_states = storage.all(State)


@app.teardown_appcontext
def teardown(exception=None):
    """ Teardown """
    storage.close()


@app.route('/states_list')
def states_list():
    """ States list """
    states = ""
    state_list = []
    for state in all_states.values():
        insort(state_list, "{},{}".format(state.name, state.id))
    for i in state_list:
        _id = i.split(',')[1]
        _name = i.split(',')[0]
        states += '\n\t<li>{}: <b>{}</b></li>\n'.format(_id, _name)
    return render('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """ Cities by state """
    cities = ""
    city_list = []
    # Create a sorted list of states
    for state in all_states.values():
        if len(state.cities) is 0:
            insort(city_list, "{},{},{},{}".format(
                state.name, "", "", state.id))
        else:
            for city in state.cities:
                insort(city_list, "{},{},{},{}".format(
                    state.name, city.name, city.id, state.id))

    state_id = ""
    for i in city_list:
        if state_id != i.split(',')[3]:
            state_id = i.split(',')[3]
            state_name = i.split(',')[0]
            city_id = i.split(',')[2]
            city_name = i.split(',')[1]
            if city_list.index(i) is not 0:
                cities += "\n\t\t</ul>\n\t</li>"
            cities += '\n\t<li>{}: <b>{}</b>\n\t\t<ul>'.format(
                state_id, state_name)
            if city_id != "":
                cities += '\n\t\t\t<li>{}: <b>{}</b></li>\n'.format(
                    city_id, city_name)
        else:
            city_id = i.split(',')[2]
            city_name = i.split(',')[1]
            if city_id != "":
                cities += '\n\t\t\t<li>{}: <b>{}</b></li>\n'.format(
                    city_id, city_name)
    cities += "\n\t\t</ul>\n\t</li>"
    return render('8-cities_by_states.html', cities=cities)


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def _states(id):
    """ States list whit filter """
    if id is None:
        states = ""
        state_list = []
        for state in all_states.values():
            insort(state_list, "{},{}".format(state.name, state.id))
        return render('9-states.html', _id=id, state_list=state_list)
    else:
        city_list = []
        for state in all_states.values():
            if state.id == id:
                for city in state.cities:
                    insort(city_list, "{},{}".format(city.name, city.id))
                return render('9-states.html', _id=id, s_name=state.name, c_list=city_list)
        return render('9-states.html', _id='No')


@app.route('/states_old', defaults={'id': None})
@app.route('/states_old/<id>')
def states_list2(id):
    """ States list whit filter """
    if id is None:
        states = ""
        state_list = []
        for state in all_states.values():
            insort(state_list, "{},{}".format(state.name, state.id))
        for i in state_list:
            _id = i.split(',')[1]
            _name = i.split(',')[0]
            states += '\n\t\t<li>{}: <b>{}</b></li>\n'.format(_id, _name)
        if len(state_list) is not 0:
            states = "\n\t<h1>States</h1>\n\t<ul>\n{}\n\t</ul>".format(states)
        return render('9-states.html', status=states)

    city_list = []
    state_id = ""
    cities = ""
    status = "\n\t<h1>Not found!</h1>"
    for state in all_states.values():
        if state.id == id:
            if len(state.cities) is 0:
                insort(city_list, "{},{},{},{}".format(
                    state.name, "", "", state.id))
                status = "\n\t<h1>State: {}</h1>\n\t<h3>Cities:</h3>\n\t<ul>\n\t</ul>".format(
                    state.name)
            else:
                for city in state.cities:
                    insort(city_list, "{},{},{},{}".format(
                        state.name, city.name, city.id, state.id))
            break

    for i in city_list:
        city_id = i.split(',')[2]
        city_name = i.split(',')[1]
        if city_id != "":
            cities += '\n\t\t<li>{}: <b>{}</b></li>\n'.format(
                city_id, city_name)
    if len(cities) is not 0:
        cities = "\t<ul>\n{}\n\t</ul>\n".format(cities)
        status = "\n\t<h1>State: {}</h1>\n\t<h3>Cities:</h3>".format(
            city_list[0].split(',')[0])
    return render('9-states.html', cities=cities, status=status)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
