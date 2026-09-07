#!/usr/bin/python3
"""Unittests for models/review.py."""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test suite for the Review class."""

    def tearDown(self):
        """Clean up temporary JSON files."""
        try:
            os.remove("file.json")
        except OSError:
            pass

    def test_is_subclass(self):
        """Test that Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_default_attributes(self):
        """Test default attribute values and types."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_to_dict(self):
        """Test to_dict method with Review attributes."""
        review = Review()
        r_dict = review.to_dict()
        self.assertEqual(type(r_dict), dict)
        self.assertEqual(r_dict["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
