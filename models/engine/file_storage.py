#!/usr/bin/python3
"""
Module to define Filestorage class

"""

import json


class FileStorage:
    """
        Its a class that serializes to a json file
        and deserializes json file to instance
        mean => class to save a file and restore it
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            method that return all objects
        """
        return self.__class__.__objects

    def new(self, obj):
        """
            method that add a new object to all objects
        """
        self.__class__.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
            method that save and make serialization to json
        """
        dict_objects = {}
        for key, value in self.__class__.__objects.items():
            dict_objects[key] = value.to_dict()
        with open(self.__class__.__file_path, 'w') as file:
            json.dump(dict_objects, file)

    def all_classes(self):
        """
            method that combine all classes and return it
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.review import Review
        from models.place import Place

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Review': Review,
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'State': State
        }

        return classes

    def reload(self):
        """
            method that deserialize the data and retraive
            it to objects
        """
        try:
            with open(self.__class__.__file_path, 'r') as file:
                content = file.read()
                if content:
                    dict_objects = json.loads(content)
                    self.__class__.__objects = {}
                    for key, value in dict_objects.items():
                        self.__class__.__objects[key] = \
                                self.all_classes()[value["__class__"]](**value)
                else:
                    self.__class__.__objects = {}
        except FileNotFoundError:
            pass
