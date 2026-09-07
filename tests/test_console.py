#!/usr/bin/python3
"""Unittests for console.py."""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test suite for the HBNBCommand command interpreter."""

    def test_prompt(self):
        """Test prompt string."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test empty line input produces no output."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit(self):
        """Test quit command exits loop."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF signal exits loop."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_missing_class(self):
        """Test create without class name."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test create with non-existent class."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
