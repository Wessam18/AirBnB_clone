#!/usr/bin/python3
"""test place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """test place class"""

    def setUp(self):
        """setup the test"""
        self.place = Place()

    def test_class_exists(self):
        """Test if class exists"""
        self.assertEqual(str(type(self.place)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_instance(self):
        """Test for an instance of Place"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test if attributes are correctly set"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """Test if attributes are of correct type"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_no_args_instantiates(self):
        """Test that no arguments instantiates Place"""
        self.assertEqual(Place, type(Place()))

    def test_id_is_public_str(self):
        """Test if id is public and is a string"""
        self.assertEqual(str, type(self.place.id))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at is public and is a datetime"""
        self.assertEqual(datetime, type(self.place.updated_at))

    def test_created_at_is_public_datetime(self):
        """Test if created_at is public and is a datetime"""
        self.assertEqual(datetime, type(self.place.created_at))

    def test_str_method(self):
        """Test if the str method has the correct output"""
        string = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(string, str(self.place))


if __name__ == "__main__":
    unittest.main()
