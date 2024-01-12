#!/usr/bin/python3
"""
    This is the base model that defines
    all common attributes, methods and other classes
"""

import uuid

from datetime import datetime
from models import storage


class BaseModel:
    """
    the base model class that all other classes inherit fom it
    """
    def __init__(self, *args, **kwargs):
        """
        Magic method to inialize attributes of the class
        Args:
            id: id for each instance from the class
            created_at: the time at which the class created
            updated_at: the time at which the class is updated
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Magic method that return string representation of a class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """method to update the time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """method return dict representation of attributes"""
        obj_dict = self.__dict__.copy()
        obj_dict.update({"__class__": self.__class__.__name__})
        obj_dict.update({"created_at": self.created_at.isoformat()})
        obj_dict.update({"updated_at": self.updated_at.isoformat()})
        return obj_dict


if __name__ == "__main__":
    BaseModel()
