######################## Imports ########################
from flask import Flask

######################## Config ########################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

from app import views