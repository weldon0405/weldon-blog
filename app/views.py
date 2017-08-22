from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Weldon'} # fake user
    return render_template('index.html', title='Home', user=user)
