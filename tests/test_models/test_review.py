#!/usr/bin/python3
"""Test module for Review"""


from datetime import datetime
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""

    def setUp(self):
        """Creates a simple object or instance of Review"""
        self.my_model = Review()

    def tearDown(self):
        """Cleanup method"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_types(self):
        """Test attribute types"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.place_id, str)
        self.assertIsInstance(self.my_model.user_id, str)
        self.assertIsInstance(self.my_model.text, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = f'[Review] ({self.my_model.id}) {self.my_model.__dict__}'
        self.assertEqual(str(self.my_model), output)


if __name__ == '__main__':
    unittest.main()
