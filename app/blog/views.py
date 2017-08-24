# app/blog/views.py

#################### Imports ####################

from flask import render_template, Blueprint
from app import app



#################### Config ####################

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')



#################### Routes ####################

@blog_blueprint.route('/')
@blog_blueprint.route('/index')
@blog_blueprint.route('/blog')
# @app.route('/')
# @app.route('/index')
def index():
    user = {'nickname': 'Weldon'} # fake user
    posts = [
        {'author': {'nickname': 'Weldon'},
         'blog_title': {'post_name': 'Example Post 1'},
         'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ligula lectus, gravida et mauris consequat, condimentum eleifend nibh. Cras rhoncus ante eu nunc dictum lacinia. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae ultricies urna. Morbi ornare tristique finibus. Maecenas ut egestas purus, in maximus libero. Maecenas sed velit tincidunt, tempor mauris id, aliquam turpis. Quisque id arcu sed arcu lacinia aliquam. Integer laoreet ipsum diam, dignissim viverra libero tincidunt sit amet. Sed euismod neque quis tellus porta, bibendum ornare urna convallis. Vivamus sollicitudin sollicitudin leo eu elementum.'
        },
        {'author': {'nickname': 'Brandy'},
         'blog_title': {'post_name': 'Example Post 2'},
         'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ligula lectus, gravida et mauris consequat, condimentum eleifend nibh. Cras rhoncus ante eu nunc dictum lacinia. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae ultricies urna. Morbi ornare tristique finibus. Maecenas ut egestas purus, in maximus libero. Maecenas sed velit tincidunt, tempor mauris id, aliquam turpis. Quisque id arcu sed arcu lacinia aliquam. Integer laoreet ipsum diam, dignissim viverra libero tincidunt sit amet. Sed euismod neque quis tellus porta, bibendum ornare urna convallis. Vivamus sollicitudin sollicitudin leo eu elementum.'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
