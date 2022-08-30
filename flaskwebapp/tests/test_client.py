import unittest
from app import create_app, db

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        '''Creates a test environment similar to PRODUCTION, includes a new database just for testing'''
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
    
    def tearDown(self):
        '''Runs after each test to remove the set up'''
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_home_page(self):
        ''' / loads with a 200 response'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

