#!/usr/bin/python3
"""test cases for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """class test the console"""
    def setUp(self):
        """Set up for the tests"""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_do_quit(self):
        """Test the do_quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_do_EOF(self):
        """Test the do_EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        """Test the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test do all"""
        self.cli.do_all('')
        self.assertEqual(mock_stdout.getvalue(), "[]\n")
        self.cli.do_all('User')
        self.assertEqual(mock_stdout.getvalue(), "[]\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test do all"""
        self.cli.do_count('User')
        self.assertEqual(mock_stdout.getvalue(), "0\n")

    def test_precmd(self):
        """Test do all"""
        self.assertEqual(
                self.cli.precmd('User.create("1234")'), 'create User 1234')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test do show"""
        self.cli.do_show('')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.do_show('User')
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")
        self.cli.do_show('User 1234')
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test do update"""
        self.cli.do_update('')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.do_update('User')
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")
        self.cli.do_update('User 1234')
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")
        self.cli.do_update('User 1234 name')
        self.assertEqual(mock_stdout.getvalue(), "** value missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test do destroy"""
        self.cli.do_destroy('')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.do_destroy('User')
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")
        self.cli.do_destroy('User 1234')
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """test create method"""
        self.cli.do_create('')
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")
        self.cli.do_create('User')
        self.assertRegex(
            mock_stdout.getvalue(),
            '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n$')


if __name__ == "__main__":
    unittest.main()
