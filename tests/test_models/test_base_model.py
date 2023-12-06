"""A module for testing Base class"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base class."""

    def setUp(self):
        """Creates a simple object or instance of BaseModel"""
        self.my_model = BaseModel()

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[BaseModel] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        actual_output = str(self.my_model)
        self.assertEqual(actual_output, output)

    def test_save(self):
        """Test the save() method method"""
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

        self.my_model.save()

        my_model_json = self.my_model.to_dict()

        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_save_updated_at(self):
        """Test if updated_at updates the time at every update"""
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        updated_updated_at = self.my_model.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_to_dict(self):
        """Test if it converts the object to_dict
        checks the types of JSON value
        """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], str(
            self.my_model.created_at.isoformat()))
        self.assertEqual(my_model_dict['updated_at'], str(
            self.my_model.updated_at.isoformat()))

if __name__ == '__main__':
    unittest.main()
