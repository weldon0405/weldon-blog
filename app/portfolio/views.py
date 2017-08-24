# app/users/views.py

#################### Imports ####################

from flask import render_template, Blueprint



#################### Config ####################

portfolio_blueprint = Blueprint('portfolio', __name__, template_folder='templates')



#################### Routes ####################

@portfolio_blueprint.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')