# app/users/views.py

#################### Imports ####################

from flask import render_template, Blueprint



#################### Config ####################

users_blueprint = Blueprint('users', __name__, template_folder='templates')



#################### Routes ####################

@users_blueprint.route('/login')
def login():
    return render_template('login.html')