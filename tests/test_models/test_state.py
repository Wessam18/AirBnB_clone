#!/usr/bin/python3
"""test state class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up for the tests"""
        self.my_state = State()

    def tearDown(self):
        """Tear down for the tests"""
        del self.my_state

    def test_is_instance_base_model(self):
        """Test if my_state is an instance of BaseModel"""
        self.assertIsInstance(self.my_state, BaseModel)

    def test_field_name(self):
        """Test the name field of State"""
        self.assertEqual(type(self.my_state.name), str)
        self.assertEqual(self.my_state.name, "")

    def test_field_name_assignment(self):
        """Test assigning value to name field of State"""
        self.my_state.name = "California"
        self.assertEqual(self.my_state.name, "California")

    def test_to_dict(self):
        """Test the to_dict method of State"""
        state_dict = self.my_state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertFalse('name' in state_dict)
        self.assertTrue('__class__' in state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_class_exist(self):
        """test for test class exist"""
        state = State()
        test = "<class 'models.state.State'>"
        self.assertEqual(str(type(state)), test)

    def test_str(self):
        """Test the __str__ method of State"""
        state_str = str(self.my_state)
        self.assertEqual(type(state_str), str)
        self.assertTrue("State" in state_str)


if __name__ == "__main__":
    unittest.main()
