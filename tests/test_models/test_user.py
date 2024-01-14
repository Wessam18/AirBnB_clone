#!/usr/bin/python3
"""test cases to test the base model class"""

import unittest
from datetime import datetime
from models.user import User


class test_User(unittest.TestCase):
    """test user class"""
    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """test attribute"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_init_with_kwargs(self):
        """test init"""
        data = {
            'id': 'user_id',
            'created_at': '2022-02-01T00:00:00',
            'updated_at': '2022-02-02T12:34:56',
            '__class__': 'User',
            'email': 'wess@example.com',
            'password': 'wess_password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**data)
        self.assertEqual(user.id, 'user_id')
        self.assertEqual(user.created_at, datetime(2022, 2, 1, 0, 0, 0))
        self.assertEqual(user.updated_at, datetime(2022, 2, 2, 12, 34, 56))
        self.assertEqual(user.email, 'wess@example.com')
        self.assertEqual(user.password, 'wess_password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_invalid_user_init(self):
        """test init"""
        data = {
            'id': 'user_test_id',
            'created_at': '2022-02-01T00:00:00',
            'updated_at': '2022-02-02T12:34:56',
            '__class__': 'User',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        user = User(**data)
        self.assertFalse(
            hasattr(user, 'extra_field'),
            f"{user.__dict__} contains 'extra_field'")


if __name__ == '__main__':
    unittest.main()
