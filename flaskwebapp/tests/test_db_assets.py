import unittest
from app import create_app, db
from app.models import Asset


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

    def test_asset_serial(self):
        ''' Tests asset serial '''
        a = Asset(serial_number='test_serial')
        self.assertTrue(a.serial_number is not None)
        self.assertTrue(a.serial_number == 'test_serial')
        self.assertFalse(a.serial_number == 'not_my_serial')

    def test_asset_model(self):
        ''' Tests device model '''
        a = Asset(device_model='MacBook Pro')
        self.assertTrue(a.device_model is not None)
        self.assertTrue(a.device_model == 'MacBook Pro')
        self.assertFalse(a.device_model == 'MacBook Air')

    def test_assigned_to(self):
        ''' Tests device assigned to '''
        a = Asset(assigned_to='GeekTechStuff')
        self.assertTrue(a.assigned_to is not None)
        self.assertTrue(a.assigned_to == 'GeekTechStuff')
        self.assertFalse(a.assigned_to == 'GeekDude')
