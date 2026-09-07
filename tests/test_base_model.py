#!/usr/bin/python3
"""Unittests for models/base_model.py."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suite for BaseModel initialization and methods."""

    def test_init_no_args(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)

    def test_str_representation(self):
        bm = BaseModel()
        self.assertIn("[BaseModel]", str(bm))
        self.assertIn(bm.id, str(bm))


if __name__ == "__main__":
    unittest.main()
