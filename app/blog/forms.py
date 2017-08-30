# app/blog/forms.py

from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class AddArticleForm(Form):
    article_title = StringField('Article Title', validators=[DataRequired()])
    article_author = StringField('Article Author', validators=[DataRequired()])
    article_content = TextAreaField('Article Content', validators=[DataRequired()])
