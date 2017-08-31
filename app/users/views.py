# app/users/views.py

#################### Imports ####################

from flask import render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError

from .forms import RegisterForm
from app import db
from app.models import User


#################### Config ####################

users_blueprint = Blueprint('users', __name__, template_folder='templates')



#################### Routes ####################

@users_blueprint.route('/login')
def login():
    return render_template('login.html')

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.username.data, form.first_name.data, form.last_name.data, form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Thank you for registering!', 'success')
                return redirect(url_for('blog.index'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
    return render_template('register.html', form=form)
