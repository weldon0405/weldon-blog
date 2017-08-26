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
    