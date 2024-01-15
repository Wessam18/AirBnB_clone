#!/usr/bin/python3
"""test cases to test the base model class"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class to test the console"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down for the tests"""
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test the do_quit command"""
        self.console.onecmd("quit")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test the do_EOF command"""
        self.console.onecmd("EOF")
        self.assertEqual(mock_stdout.getvalue(), '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test the emptyline command"""
        self.console.onecmd("\n")
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test do_all command"""
        self.console.onecmd('all User')
        self.assertEqual(mock_stdout.getvalue(), '[]\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test do_count command"""
        self.console.onecmd('count User')
        self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test do_show command"""
        self.console.onecmd('show')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test do_update command"""
        self.console.onecmd('update')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test do_destroy command"""
        self.console.onecmd('destroy')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test do_create command"""
        self.console.onecmd('create User')
        output = mock_stdout.getvalue().strip()
        self.assertIsNotNone(output)
        self.assertRegex(
            output,
            '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_do_update_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('create User')
            instance_id = output.getvalue().strip()

            self.console.onecmd(f'update User {instance_id} age 25')
            self.console.onecmd(f'show User {instance_id}')

            # Verify that the 'age' attribute has been updated
            self.assertIn("'age': 25", output.getvalue().strip())

    def test_help_update(self):
        h = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Update a class instance of a given id by adding or updating\n   "
             "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
