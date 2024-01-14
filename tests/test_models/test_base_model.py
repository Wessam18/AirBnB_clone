#!/usr/bin/python3
"""to test base model class"""

import unittest
import pycodestyle
import uuid
import models
import inspect
from datetime import datetime, timedelta
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    def setUp(self):
        """setup the test"""
        self.model = BaseModel()

    def test_base_model(self):
        """test instance"""
        my_obj = BaseModel()
        self.assertIsInstance(my_obj, BaseModel)

    def test_created_at_type(self):
        """test type of instance"""
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """test update method"""
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_basemodel_id(self):
        """test id"""
        my_Id1 = BaseModel()
        my_Id2 = BaseModel()
        self.assertNotEqual(my_Id1.id, my_Id2.id)

    def test_id_type(self):
        """test id type"""
        self.assertEqual(type(self.model.id), str)

    def test_basemodel_str(self):
        """test str"""
        my_str = BaseModel()
        my_dict = my_str.__dict__
        str1 = f"[BaseModel] ({my_str.id}) {my_dict}"
        str2 = str(my_str)
        self.assertEqual(str1, str2)

    def test_basemodel_str_method(self):
        """test str"""
        str_representation = str(self.model)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.model.id, str_representation)
        self.assertIn(str(self.model.__class__.__name__), str_representation)

    def test_basemodel_save(self):
        """test save method"""
        first_time = self.model.updated_at
        self.model.save()
        second_time = self.model.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_basemodel_pycodestyle(self):
        """test pycodestyle"""
        betty = pycodestyle.StyleGuide(ignore=['E501', 'W503'])
        my_path = "models/base_model.py"
        res = betty.check_files([my_path])
        self.assertEqual(res.total_errors, 0)

    def test_basemodel_doc(self):
        """test decomentation"""
        self.assertIsNotNone(BaseModel.__doc__, 'no docs for BaseModel Class')
        self.assertIsNotNone(
            inspect.getdoc(models.base_model), 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_to_dict_method(self):
        """test dict method"""
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_invalid_initialization(self):
        """test init"""
        invalid_dict = {
            "id": "id-32",
            "created_at": "today",
            "updated_at": "1111102223",
            "__class__": "abc"
            }
        with self.assertRaises(ValueError):
            BaseModel(**invalid_dict)

    def test_default_instance(self):
        """test init"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_instance_with_kwargs(self):
        """test init with kwargs"""
        valid_dict = {
            "id": "id-32",
            "created_at": "2024-01-10T22:40:45.795104",
            "updated_at": "2024-01-10T22:40:45.795104",
            "__class__": "BaseModel"
            }
        bm = BaseModel(**valid_dict)
        self.assertEqual(bm.id, "id-32")
        self.assertEqual(
            bm.created_at, datetime(2024, 1, 10, 22, 40, 45, 795104))
        self.assertEqual(
            bm.updated_at, datetime(2024, 1, 10, 22, 40, 45, 795104))
        self.assertEqual(bm.to_dict()["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
