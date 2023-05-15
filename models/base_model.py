#!/usr/bin/python3
"""Defining a class"""
from _datetime import datetime
import uuid
import models

class BaseModel:
    """Representing a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class
        Args:
            id - string assign to uuid
            created_at - datetime instance
            updated_at - updated daytime instance
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the class"""
        class_name = self.__class__.__name__
        rep = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return rep

    def save(self):
        """Update the updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dict containing all key and value of dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

