#!/usr/bin/python3
"""Test module for user"""


from datetime import datetime
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class"""

    def setUp(self):
        """Creates a simple object or instance of User"""
        self.my_model = User()

    def tearDown(self):
        """Cleanup method"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.email, str)
        self.assertIsInstance(self.my_model.password, str)
        self.assertIsInstance(self.my_model.first_name, str)
        self.assertIsInstance(self.my_model.last_name, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = f'[User] ({self.my_model.id}) {self.my_model.__dict__}'
        self.assertEqual(str(self.my_model), output)


if __name__ == '__main__':
    unittest.main()
