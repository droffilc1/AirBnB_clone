#!/usr/bin/python3
"""Test module for Amenity"""


from datetime import datetime
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        """Creates a simple object or instance of Amenity"""
        self.my_model = Amenity()

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
        output = f'[Amenity] ({self.my_model.id}) {self.my_model.__dict__}'
        self.assertEqual(str(self.my_model), output)
