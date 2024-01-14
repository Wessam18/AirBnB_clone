#!/usr/bin/python3
"""to test amenity class"""

import unittest
import models
import os
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from unittest.mock import patch


class TestAmenity(unittest.TestCase):
    """testing Amenity class"""

    @classmethod
    def setUpClass(cls):
        """test setup"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """to test the class"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_docstring(self):
        """Test if module and class have docstring."""
        self.assertIsNotNone(models.amenity.__doc__, 'No docs for module')
        self.assertIsNotNone(Amenity.__doc__, 'No docs for class')

    def test_execution(self):
        """Test if file has permissions to execute."""
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """Test if an object is an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Test if Amenity has the required attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_ids(self):
        """Test that id is unique."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_at(self):
        """Test that created_at is a datetime instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at is a datetime instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_created_updated_at_equal(self):
        """Test that created_at and updated_at are equal at instantiation."""
        amenity = Amenity()
        self.assertEqual(amenity.created_at, amenity.updated_at)

    def test_created_updated_at_unique(self):
        """Test that created_at and updated_at are unique for two instances."""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        """Test str representation of Amenity."""
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + repr(dt), amenity_str)
        self.assertIn("'updated_at': " + repr(dt), amenity_str)

    def test_init_with_kwargs(self):
        """Test instantiation with kwargs."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_init_with_None_kwargs(self):
        """Test instantiation with None kwargs."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_save_method(self):
        """Test save method."""
        with patch('models.storage.save') as mock_save:
            amenity = Amenity()
            amenity.save()
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        """Test to_dict method."""
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_save_updates_file(self):
        """Test that save method updates file."""
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())

    def test_contrast_to_dict_dunder_dict(self):
        """Test that to_dict is different from __dict__."""
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict with argument."""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
