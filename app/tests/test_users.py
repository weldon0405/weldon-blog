# app/tests/test_users.py

import os
import unittest

from app import app, db

class UsersTests(unittest.TestCase):

#################### setup and teardown ####################

    # executed prior  to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://malbwa:Cypre$$44W@localhost/test'
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

#################### Helper Methods ####################

    def register(self, username, first_name, last_name, email, password, confirm):
        return self.app.post('/register', data=dict(username=username, first_name=first_name, last_name=last_name, email=email, password=password, confirm=confirm), follow_redirects=True)



#################### Tests ####################

    def test_user_registration_form_displays(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please Register Your New Account', response.data)

    def test_valid_user_registration(self):
        self.app.get('/register', follow_redirects=True)
        response = self.register('weldon', 'Weldon', 'Malbrough', 'weldon0405@yahoo.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertIn(b'Thank you for registering!', response.data)

    def test_duplicate_email_user_registration_error(self):
        self.app.get('/register', follow_redirects=True)
        self.register('weldon', 'Weldon', 'Malbrough', 'weldon0405@yahoo.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.app.get('/register', follow_redirects=True)
        response = self.register('weldon', 'Weldon', 'Malbrough', 'weldon0405@yahoo.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        self.assertIn(b'ERROR! Email (weldon0405@yahoo.com) already exists.', response.data)

    def test_missing_field_user_registration_error(self):
        self.app.get('/register', follow_redirects=True)
        response = self.register(' ', ' ', ' ', 'weldon0405@yahoo.com', 'FlaskIsAwesome', '')
        self.assertIn(b'This field is required.', response.data)

if __name__ == '__main__':
    unittest.main()