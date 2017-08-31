# app/models.py

from app import db
from sqlalchemy import Column, DateTime
from datetime import datetime



class Blog(db.Model):

    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String, nullable=False)
    article_author = db.Column(db.String, nullable=False)
    pub_date = db.Column(DateTime, default=datetime.utcnow)
    article_content = db.Column(db.String, nullable=False)

    def __init__(self, title, author, content):
        self.article_title = title
        self.article_author = author
        self.article_content = content

    def __repr__(self):
        return 'title {}'.format(self.name)



class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_plaintext = db.Column(db.String, nullable=False) ######TEMPORARY -- MUST HASH THE PASSWORD AND DELETE

    def __init__(self, username, first_name, last_name, email, password_plaintext):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_plaintext = password_plaintext

    def __repr__(self):
        return '<User {0}>'.format(self.name)
    