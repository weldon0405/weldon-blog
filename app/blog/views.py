# app/blog/views.py

#################### Imports ####################

from flask import render_template, Blueprint, request, redirect, url_for, flash
from app import app
from app import db
from app.models import Blog
from .forms import AddArticleForm



#################### Config ####################

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')



#################### Helper Functions ####################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'info')



#################### Routes ####################

@blog_blueprint.route('/')
@blog_blueprint.route('/index')
@blog_blueprint.route('/blog')
def index():
    all_articles = Blog.query.all()
    return render_template('blog.html', articles=all_articles)

@blog_blueprint.route('/add_article', methods=['GET', 'POST'])
def add_article():
    form = AddArticleForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_article = Blog(form.article_title.data, form.article_author.data, form.article_content.data)
            db.session.add(new_article)
            db.session.commit()
            flash('New Article, {}, added!'.format(new_article.article_title), 'success')
            return redirect(url_for('blog.index'))
        else:
            flash_errors(form)
            flash('ERROR! Article was not added.', 'error')

    return render_template('add_article.html', form=form)