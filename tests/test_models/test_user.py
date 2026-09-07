#!/usr/bin/python3
"""Unittests for models/user.py."""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test suite for the User class."""

    def tearDown(self):
        """Clean up temporary JSON files."""
        try:
            os.remove("file.json")
        except OSError:
            pass

    def test_is_subclass(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_default_attributes(self):
        """Test default attribute values and types."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_attribute_assignment(self):
        """Test assigning values to User attributes."""
        user = User()
        user.first_name = "Betty"
        user.last_name = "Bar"
        user.email = "airbnb@holbertonshool.com"
        user.password = "root"
        self.assertEqual(user.first_name, "Betty")
        self.assertEqual(user.last_name, "Bar")
        self.assertEqual(user.email, "airbnb@holbertonshool.com")
        self.assertEqual(user.password, "root")

    def test_to_dict(self):
        """Test to_dict method with User attributes."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)


if __name__ == "__main__":
    unittest.main()
