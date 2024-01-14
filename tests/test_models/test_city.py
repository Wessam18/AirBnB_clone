#!/usr/bin/pyhon3
"""to test city class"""

import unittest
import os
from datetime import datetime
from time import sleep
from unittest.mock import patch
from models.city import City


class testCity(unittest.TestCase):
    """test city class"""
    def setUp(self):
        """setup the test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """setup the test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_city_instance(self):
        """test init"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """test attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_two_cities_ids(self):
        """test id"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_cities_created_at(self):
        """test create at"""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_cities_updated_at(self):
        """test updateat"""
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    # ... (Include other city-specific tests)

    def test_save_method(self):
        """test save method"""
        with patch('models.storage.save') as mock_save:
            city = City()
            city.save()
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        """test dict"""
        city = City()
        obj_dict = city.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    # ... (Include other to_dict tests)

    def test_instantiation_with_kwargs(self):
        """test init"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """test init"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == '__main__':
    unittest.main()
