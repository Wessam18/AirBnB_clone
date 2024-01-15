#!/usr/bin/python3
"""Test cases for the HBNBCommand class"""

import os
import unittest
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    @classmethod
    def setUpClass(cls):
        """Set up class for the tests"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        storage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down class after the tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        """Set up for each test"""
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        """Tear down after each test"""
        pass

    # Existing Tests

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit_command(self, mock_stdout):
        """Test the do_quit command"""
        self.hbnb_command.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF_command(self, mock_stdout):
        """Test the do_EOF command"""
        self.hbnb_command.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line_command(self, mock_stdout):
        """Test the empty_line command"""
        self.hbnb_command.onecmd("\n")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_command(self, mock_stdout):
        """Test do_all command"""
        self.hbnb_command.onecmd('all User')
        self.assertEqual(mock_stdout.getvalue(), '[]\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count_command(self, mock_stdout):
        """Test do_count command"""
        self.hbnb_command.onecmd('count User')
        self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_command(self, mock_stdout):
        """Test do_show command"""
        self.hbnb_command.onecmd('show')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_command(self, mock_stdout):
        """Test do_update command"""
        self.hbnb_command.onecmd('update')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy_command(self, mock_stdout):
        """Test do_destroy command"""
        self.hbnb_command.onecmd('destroy')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_command(self, mock_stdout):
        """Test do_create command"""
        self.hbnb_command.onecmd('create User')
        output = mock_stdout.getvalue().strip()
        self.assertIsNotNone(output)
        self.assertRegex(
            output,
            '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_do_update_instance(self):
        """Test updating an instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.hbnb_command.onecmd('create User')
            instance_id = output.getvalue().strip()

            self.hbnb_command.onecmd(f'update User {instance_id} age 25')
            self.hbnb_command.onecmd(f'show User {instance_id}')

            # Verify that the 'age' attribute has been updated
            self.assertIn("'age': 25", output.getvalue().strip())

    def test_help_update_command(self):
        """Test the help_update command"""
        expected_output = (
            "Usage: update <class> <id> <attribute_name> <attribute_value> or"
            "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
            ">) or\n       <class>.update(<id>, <dictionary>)\n        "
            "Update a class instance of a given id by adding or updating\n   "
            "     a given attribute key/value pair or dictionary."
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.hbnb_command.onecmd("help update"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_prompt_string(self):
        """Test the prompt string"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line_command(self):
        """Test the empty_line command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit_exits_command(self):
        """Test quitting the command"""
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits_command(self):
        """Test exiting with EOF"""
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_missing_class_command(self):
        """Test creating with a missing class"""
        expected_output = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_class_command(self):
        """Test creating with an invalid class"""
        expected_output = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_syntax_command(self):
        """Test creating with invalid syntax"""
        expected_output = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        expected_output = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_object_command(self):
        """Test creating objects with valid syntax"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "User.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "State.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "City.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(test_key, storage.all().keys())

    # Additional Tests

    def test_quit_command(self):
        """Test the quit command"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_command(self):
        """Test the EOF command"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all_command(self):
        """Test the all command"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show_command(self):
        """Test the show command"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_class_name_command(self):
        """Test the show command with missing class name"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name2_command(self):
        """Test the show command with missing instance id"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    def test_show_no_instance_found_command(self):
        """Test the show command with non-existing instance id"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "124356876")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create_command(self):
        """Test the create command"""
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name_command(self):
        """Test the create command with missing class name"""
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doesnt_exist_command(self):
        """Test the create command with non-existing class"""
        console = self.create()
        console.onecmd("create Binita")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    def test_update_valid_dictionary_dot_notation(self):
        """Test updating with a valid dictionary using dot notation"""
        self._test_update_valid_dictionary_notation(
            "{}.update({{'attr_name': 'attr_value'}})")

    def test_update_valid_dictionary_with_int_space_notation(self):
        """Test updating with a valid
        dictionary with int using space notation"""
        self._test_update_valid_dictionary_notation(
            "update Place {} {'max_guest': 98})")

    def test_update_valid_dictionary_with_int_dot_notation(self):
        """Test updating with a valid dictionary with int using dot notation"""
        self._test_update_valid_dictionary_notation(
            "Place.update({}, {'max_guest': 98})")

    def test_update_valid_dictionary_with_float_space_notation(self):
        """Test updating with a valid dictionary
        with float using space notation"""
        self._test_update_valid_dictionary_notation(
            "update Place {} {'latitude': 9.8})")

    def test_update_valid_dictionary_with_float_dot_notation(self):
        """Test updating with a valid
        dictionary with float using dot notation"""
        self._test_update_valid_dictionary_notation(
            "Place.update({}, {'latitude': 9.8})")

    def _test_update_valid_dictionary_notation(self, test_cmd):
        """Helper method for testing update with valid dictionary notation"""
        classes = ["BaseModel",
                   "User", "State", "City", "Place", "Amenity", "Review"]

        for class_name in classes:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {class_name}")
                test_id = output.getvalue().strip()

            test_cmd_instance = test_cmd.format(class_name, test_id)
            HBNBCommand().onecmd(test_cmd_instance)
            test_dict = storage.all()[f"{class_name}.{test_id}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])


if __name__ == '__main__':
    unittest.main()
