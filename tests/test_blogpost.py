from datetime import datetime, timedelta
import unittest
from .app import db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.user_mike = User(id=1,username = 'kenm',password = 'strong', email = 'yaya@ms.com')

    def tearDown(self):
        User.query.delete()
    def test_password_hashing(self):
        u = User(username='kama')
        u.set_password('5432')
        self.assertFalse(u.check_password('pass123'))
        self.assertTrue(u.check_password('5432'))
    def test_save_user(self):
    def test_check_instance_variables(self):
        self.assertEquals(self.user_mike.username,'kenm')
        self.assertEquals(self.user_mike.password,'strong')
        self.assertEquals(self.user_mike.email,"yaya@ms.com")
    