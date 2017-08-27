# app/blog/views.py

#################### Imports ####################

from flask import render_template, Blueprint
from app import app
from app.models import Blog



#################### Config ####################

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')



#################### Routes ####################

@blog_blueprint.route('/')
@blog_blueprint.route('/index')
@blog_blueprint.route('/blog')
def index():
    all_articles = Blog.query.all()
    return render_template('blog.html', articles=all_articles)
