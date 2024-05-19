#!/usr/bin/python3
"""
Defines unittests for console.py.
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand, deleteObjectById, findObjectById
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel


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
    """   Test documents for the HBNBCommand class    """
    """------------------------------------------------"""
    def test_deleteObjById_doc(self):
        """Test doc"""
        self.assertIsNotNone(deleteObjectById.__doc__)

    def test_findObjById_doc(self):
        """Test doc"""
        self.assertIsNotNone(findObjectById.__doc__)

    def test_class_doc(self):
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

    def test_do_create_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)

    def test_do_destroy_doc(self):
        """Test doc"""
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)


class TestHBNBCommand_help(unittest.TestCase):
    """   Test help of all methods inside class    """
    """------------------------------------------------"""

    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("Create a new instance of a specified \
        class and save it to the storage.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = ("Display the string representation of an instance \
        based on the class name")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Delete an instance of a specified class based on its ID.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Print all string representations of objects or \
        all objects of a specified class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = ("Count the number of instances of a specified class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Retrieve all instances or instances of a specific class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommandCreate(unittest.TestCase):
    """     Test create command of HBNBCommand   """
    """-------------------------------------------"""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_no_class_name(self, mock_stdout):
        """Test create command with no class name."""
        self.console.onecmd("create")
        self.assertIn("** class name missing **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class_name(self, mock_stdout):
        """Test create command with an invalid class name."""
        self.console.onecmd("create NonExistentClass")
        self.assertIn("** class doesn't exist **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_class_name(self, mock_stdout):
        """Test create command with a valid class name."""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertNotIn("** class doesn't exist **", output)
        self.assertNotIn("** class name missing **", output)


class TestHBNBCommandShow(unittest.TestCase):
    """Tests the show command of HBNBCommand."""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()

        # Create a sample object for testing
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """Clean up test environment."""
        storage.all().clear()

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_class_name(self, mock_stdout):
        """Test show command with no class name."""
        self.console.onecmd("show")
        self.assertIn("** class name missing **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class_name(self, mock_stdout):
        """Test show command with an invalid class name."""
        self.console.onecmd("show NonExistentClass")
        self.assertIn("** class doesn't exist **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_instance_id(self, mock_stdout):
        """Test show command with no instance ID."""
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_instance_id_not_found(self, mock_stdout):
        """Test show command with an instance ID that does not exist."""
        string = "show BaseModel 12345678-1234-1234-1234-123456789012"
        self.console.onecmd(string)
        self.assertIn("** no instance found **",
                      mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_valid_class_name_and_instance_id(self, mock_stdout):
        """Test show command with a valid class name and instance ID."""
        self.console.onecmd(f"show BaseModel {self.model.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[BaseModel] ({self.model.id})", output)
        self.assertIn(f"'id': '{self.model.id}'", output)


class TestHBNBCommandDestroy(unittest.TestCase):
    """Tests the show command of HBNBCommand."""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        storage.__objects.clear()

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_no_class_name(self, mock_stdout):
        self.console.onecmd("destroy")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class_name(self, mock_stdout):
        self.console.onecmd("destroy InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_no_instance_id(self, mock_stdout):
        self.console.onecmd("destroy BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_instance_id_not_exist(self, mock_stdout):
        self.console.onecmd("destroy BaseModel non_existent_id")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_valid_class_name_and_id(self, mock_stdout):
        # Create a new instance
        instance = BaseModel()
        instance_id = instance.id
        storage.new(instance)
        storage.save()
        # Test destruction
        self.console.onecmd(f"destroy BaseModel {instance_id}")
        self.assertEqual(mock_stdout.getvalue(), "")

        # Check if the instance is removed
        self.assertNotIn(f"BaseModel.{instance_id}", storage.all())


if __name__ == '__main__':
    unittest.main()
