# app/tests/test_users.py

import unittest

from app import app

class ProjectTests(unittest.TestCase):

#################### setup and teardown ####################

    # executed prior  to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass


#################### Tests ####################

    def test_main_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b"Future location to login to Weldon's Blog and Portfolio", response.data)

if __name__ == '__main__':
    unittest.main()