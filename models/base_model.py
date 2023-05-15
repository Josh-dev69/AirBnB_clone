#!/usr/bin/python3
"""Defining a class"""
from _datetime import datetime
import uuid
from models import storage

class BaseModel:
    """Representing a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializing the BaseModel class
        Args:
            id - string assign to uuid
            created_at - datetime instance
            updated_at - updated daytime instance
        """

        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of the class"""
        rep = f"[(self.__class__.__name__)] ({self.id}) {self.__dict__}"
        return rep

    def save(self):
        """Update the updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dict containing all key and value of dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

