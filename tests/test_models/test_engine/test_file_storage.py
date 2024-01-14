#!/usr/bin/python3
"""test the storage of data"""

import unittest
import os
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the file storage class"""

    def test_file_path(self):
        """Test the file Path"""
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test the __objects attribute"""
        self.file_storage.new(self.test_model)
        key = f"BaseModel.{self.test_model.id}"
        self.assertIn(key, self.file_storage._FileStorage__objects)
        self.assertEqual(
                self.file_storage._FileStorage__objects[key], self.test_model)

    def setUp(self):
        """Set up for the tests"""
        self.file_storage = FileStorage()
        self.test_model = BaseModel()
        self.test_model.name = "Test"
        self.test_model.save()

    def test_init(self):
        """Test the __init__"""
        new_model = BaseModel(name="Test", number=42)
        self.assertEqual(new_model.name, "Test")
        self.assertEqual(new_model.number, 42)

    def testClassInstance(self):
        """Test the class instance"""
        self.assertIsInstance(storage, FileStorage)

    def tearDown(self):
        """Tear down for the tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(f"BaseModel.{self.test_model.id}", objects)
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)
        self.assertIs(objects, self.file_storage._FileStorage__objects)

    def test_reload_file(self):
        """Test FileStorage reload"""
        self.file_storage.new(self.test_model)
        self.file_storage.save()
        FileStorage.__objects = {}
        self.file_storage.reload()
        objects = self.file_storage.all()
        key = f"BaseModel.{self.test_model.id}"
        self.assertIn(key, objects)

    def test_new(self):
        """Test the new method"""
        new_model = BaseModel()
        new_model.name = "New"
        self.file_storage.new(new_model)
        objects = self.file_storage.all()
        self.assertIn(f"BaseModel.{new_model.id}", objects)

    def testStoreBaseModel(self):
        """Test the storage of a BaseModel"""
        objects = self.file_storage.all()
        self.assertIn(f"BaseModel.{self.test_model.id}", objects)
        self.assertEqual(self.test_model.name, "Test")

    def testStoreBaseModelMyModel(self):
        """ Test save and reload """
        new_model = BaseModel()
        new_model.name = "new BaseModel"
        new_model.save()
        objectToDict = new_model.to_dict()
        allObjects = storage.all()
        key = objectToDict['__class__'] + '.' + objectToDict['id']
        self.assertEqual(key in allObjects, True)
        self.assertEqual(allObjects[key].to_dict(), objectToDict)

    def testStoreBaseModel2(self):
        """Test the storage of a BaseModel"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.save()
        objectTODict = my_model.to_dict()
        allObjects = storage.all()
        key = objectTODict['__class__'] + '.' + objectTODict['id']
        self.assertEqual(key in allObjects, True)
        self.assertEqual(objectTODict['name'], "Holberton")

        createTime1 = objectTODict['created_at']
        updateTime1 = objectTODict['updated_at']
        self.assertEqual(createTime1, updateTime1)

        my_model.name = "School"
        my_model.save()
        objectTODict = my_model.to_dict()
        allObjects = storage.all()
        self.assertEqual(key in allObjects, True)

        createTime2 = objectTODict['created_at']
        updateTime2 = objectTODict['updated_at']
        self.assertEqual(createTime1, createTime2)
        self.assertNotEqual(updateTime1, updateTime2)
        self.assertEqual(objectTODict['name'], "School")

    def test_save(self):
        """Test the save method"""
        self.file_storage.save()
        with open("file.json", "r") as file:
            objects = json.load(file)
        self.assertIn(f"BaseModel.{self.test_model.id}", objects)
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testHasAttributes(self):
        """Test the attributes of the BaseModel"""
        self.assertTrue(hasattr(self.test_model, "id"))
        self.assertTrue(hasattr(self.test_model, "created_at"))
        self.assertTrue(hasattr(self.test_model, "updated_at"))
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_reload(self):
        """Test the reload method"""
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertIn(f"BaseModel.{self.test_model.id}", objects)

    def test_reload2(self):
        """Test the reload method"""
        self.file_storage.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        objects = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(objects, FileStorage._FileStorage__objects)
        self.file_storage.reload()
        for key, value in objects.items():
            self.assertEqual(objects[key].to_dict(), value.to_dict())

    def test_save_self(self):
        """ check save self """
        msg = "FileStorage.save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)
        self.assertEqual(str(e.exception), msg)

    def test_all_classes(self):
        """Test the all_classes method"""
        classes = self.file_storage.all_classes()
        self.assertIsInstance(classes, dict)
        self.assertIn('BaseModel', classes)
        self.assertIn('User', classes)
        self.assertIn('Review', classes)
        self.assertIn('Amenity', classes)
        self.assertIn('City', classes)
        self.assertIn('Place', classes)
        self.assertIn('State', classes)

    def test_save_FileStorage(self):
        """Test if new method is working good"""
        new_model = BaseModel()
        dict_model = new_model.to_dict()
        key = dict_model['__class__'] + "." + dict_model['id']
        storage.save()
        with open("file.json", "r") as file:
            dict2 = json.load(file)
        new_dict = dict2[key]
        for key in new_dict:
            self.assertEqual(dict_model[key], new_dict[key])


if __name__ == '__main__':
    unittest.main()
