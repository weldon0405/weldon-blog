# app/tests/test_blog.py

import os
import unittest

from app import app, db
from app.models import Blog

TEST_DB = 'test.db'


class ProjectTests(unittest.TestCase):


#################### setup and teardown ####################

    # executed prior  to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost/test'
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()


#################### Tests ####################

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Blog', response.data)
        self.assertIn(b'Add Article', response.data)

    def test_main_page_query_results(self):
        response = self.app.get('/add_article', follow_redirects=True)
        self.assertIn(b'Add Article', response.data)

    def test_add_article(self):
        response = self.app.post('/add_article', data=dict(article_title='Test Article', article_author='Test Author', article_content='This is my Test Article'), follow_redirects=True)
        self.assertIn(b'New Article, Test Article, added!', response.data)

    def test_add_invalid_recipe(self):
        response = self.app.post('/add_article', data=dict(article_title='', article_author='Test Author', article_content='This is my Test Article'), follow_redirects=True)
        self.assertIn(b'ERROR! Article was not added.', response.data)
        self.assertIn(b'This field is required.', response.data)

if __name__ == '__main__':
    unittest.main()
