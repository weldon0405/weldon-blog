######################## Imports ########################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



######################## Config ########################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)



######################## Blueprints ########################

from app.users.views import users_blueprint
from app.blog.views import blog_blueprint
from app.portfolio.views import portfolio_blueprint

# Register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(portfolio_blueprint)