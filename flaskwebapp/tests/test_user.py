import unittest
from app import create_app, db


class ClientUserTestCase(unittest.TestCase):
    def setUp(self):
        '''Creates a test environment similar to PRODUCTION, includes a new database just for testing'''
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
    
    def tearDown(self):
        '''Runs after each test to remove the set up'''
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_homepage_pre_login(self):
        '''Check homepage does not show search box when user not logged in'''
        response = self.client.get('/')
        self.assertFalse('serial' in response.get_data(as_text=True))
    
    def test_register_user(self):
        '''Check a user can register'''
        response = self.client.post('/auth/register', data={
            'email':'test@geektechstuff.com',
            'username':'test_user',
            'password':'test_password',
            'password2':'test_password'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_login_user(self):
        '''Checks a user can login'''
        # Create account
        response = self.client.post('/auth/register', data={
            'email':'test@geektechstuff.com',
            'username':'test_user',
            'password':'test_password',
            'password2':'test_password'
        })
        # Log in account
        response = self.client.post('/auth/login', data={
            'email':'test@geektechstuff.com',
            'password':'test_password',
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Log Out' in response.get_data(as_text=True))
    
    def test_logout_user(self):
        '''Checks log out works'''
        # Create account
        response = self.client.post('/auth/register', data={
            'email':'test@geektechstuff.com',
            'username':'test_user',
            'password':'test_password',
            'password2':'test_password'
        })
        # Log in account
        response = self.client.post('/auth/login', data={
            'email':'test@geektechstuff.com',
            'password':'test_password',
        }, follow_redirects=True)
        # Log out account
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertTrue('logged out' in response.get_data(as_text=True))
        self.assertFalse('serial' in response.get_data(as_text=True))


    def test_homepage_post_login(self):
        '''Tests that home page displays options for logged in user'''
        # Create account
        response = self.client.post('/auth/register', data={
            'email':'test@geektechstuff.com',
            'username':'test_user',
            'password':'test_password',
            'password2':'test_password'
        })
        # Log in account
        response = self.client.post('/auth/login', data={
            'email':'test@geektechstuff.com',
            'password':'test_password',
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Check for word Serial in home page text
        self.assertTrue('Serial' in response.get_data(as_text=True))
