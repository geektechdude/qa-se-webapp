import unittest
from flask import current_app
from app import create_app, db

class appCanRun(unittest.TestCase):
    def setUp(self):
        '''Creates a test environment similar to PRODUCTION, includes a new database just for testing'''
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all
    
    def tearDown(self):
        '''Runs after each test to remove the set up'''
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_doesAppExist(self):
        '''Checks the app exists, i.e. it has started without failing'''
        self.assertFalse(current_app is None)
    
    def test_app_is_in_test_mode(self):
        '''Checks the app is running with TEST config, i.e. it's not running in PRODUCTION'''
        self.assertTrue(current_app.config['TEST'])