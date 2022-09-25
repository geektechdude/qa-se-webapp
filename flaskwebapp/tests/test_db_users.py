import unittest
from app import create_app, db
from app.models import User


class ModelUserTest(unittest.TestCase):
    def setUp(self):
        '''Creates a test environment similar to PRODUCTION'''
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        '''Runs after each test to remove the set up'''
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        ''' User Password can be set '''
        u = User(password='geektechstuff')
        self.assertTrue(u.password_hash is not None)

    def test_verify_password(self):
        ''' verify_password function returns false for wrong password '''
        u = User(password='geektechstuff')
        self.assertTrue(u.verify_password('geektechstuff'))
        self.assertFalse(u.verify_password('GeekTechStuff'))

    def test_random_salting(self):
        ''' Passwords are randomly salted '''
        u1 = User(password='geektechstuff')
        u2 = User(password='geektechstuff')
        self.assertTrue(u1.password_hash != u2.password_hash)
