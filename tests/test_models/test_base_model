#!/usr/bin/python3
"""Unittests for models/base_model.py."""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class."""

    def tearDown(self):
        """Clean up temporary JSON files."""
        try:
            os.remove("file.json")
        except OSError:
            pass

    def test_init_no_args(self):
        """Test instantiation with no arguments."""
        bm = BaseModel()
        self.assertEqual(type(bm), BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ output formatting."""
        bm = BaseModel()
        string_repr = str(bm)
        self.assertIn("[BaseModel]", string_repr)
        self.assertIn(bm.id, string_repr)

    def test_save(self):
        """Test save method updates updated_at."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict(self):
        """Test to_dict method dictionary output."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(type(bm_dict), dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
