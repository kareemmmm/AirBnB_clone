#!/usr/bin/python3
"""Unittests for models/engine/file_storage.py."""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test suite for FileStorage class methods."""

    def setUp(self):
        """Reset storage before each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up generated JSON file after tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, models.storage.all())

    def test_save_creates_file(self):
        """Test that save() creates file.json."""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that reload() loads objects back from file.json."""
        bm = BaseModel()
        bm.save()
        models.storage.all().clear()
        models.storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, models.storage.all())


if __name__ == "__main__":
    unittest.main()
