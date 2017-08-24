from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Weldon'} # fake user
    posts = [
        {'author': {'nickname': 'Weldon'},
         'blog_title': {'post_name': 'Example Post 1'},
         'body': {'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ligula lectus, gravida et mauris consequat, condimentum eleifend nibh. Cras rhoncus ante eu nunc dictum lacinia. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae ultricies urna. Morbi ornare tristique finibus. Maecenas ut egestas purus, in maximus libero. Maecenas sed velit tincidunt, tempor mauris id, aliquam turpis. Quisque id arcu sed arcu lacinia aliquam. Integer laoreet ipsum diam, dignissim viverra libero tincidunt sit amet. Sed euismod neque quis tellus porta, bibendum ornare urna convallis. Vivamus sollicitudin sollicitudin leo eu elementum.'}
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
