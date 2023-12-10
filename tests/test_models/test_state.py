#!/usr/bin/python3
"""Test module for State"""


from datetime import datetime
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        """Creates a simple object or instance of State"""
        self.my_model = State()

    def tearDown(self):
        """Cleanup method"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.name, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = f'[State] ({self.my_model.id}) {self.my_model.__dict__}'
        self.assertEqual(str(self.my_model), output)

if __name__ == '__main__':
    unittest.main()
