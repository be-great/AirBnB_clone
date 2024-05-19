#!/usr/bin/python3
"""
Defines unittests for console.py.
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_HBNBCommand_Prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    """                Test prompt                  """
    """------------------------------------------------"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    """                Test Empty line                  """
    """------------------------------------------------"""
    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_line_no_output(self, mock_stdout):
        """Test that an empty line does not produce any output."""
        command_instance = HBNBCommand()
        command_instance.onecmd("")  # Simulate entering an empty line
        output = mock_stdout.getvalue().strip()  # Get the printed output
        self.assertEqual("", output, "Expected no output for an empty line")


class test_HBNBCommand_doc(unittest.TestCase):
    """Unittests for testing doc of all methods."""

    """   Test documents for the base_model.py file    """
    """------------------------------------------------"""
    def test_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_do_EOF_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)

    def test_do_quit_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)

    def test_do_all_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)

    def test_do_update_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_do_count_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_do_show_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)

    def test_default_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.default.__doc__)

