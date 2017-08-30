# app/blog/forms.py

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired



class AddArticleForm(Form):
    article_title = StringField('Article Title', validators=[DataRequired()])
    article_author = StringField('Article Author', validators=[DataRequired()])
    article_content = StringField('Article Content', validators=[DataRequired()])
