#!/usr/bin/python3
"""Defining a class"""
from _datetime import datetime
import uuid


class BaseModel:
    """Representing a BaseModel class"""

    def __init__(self):
        """Initializing the BaseModel class
        Args:
            id - string assign to uuid
            created_at - datetime instance
            updated_at - updated daytime instance
        """
        self.id = str(uuid.uuid4())
        self.created = datetime.now()
        self.updated_at = datetime.now()

        # Checking if arguments were passed to the function
        if kwargs:
            # Loop and set the corresponding argument
            for key, value in kwargs.items():
                # Ignore the "__class__" argument
                if key == "__class__":
                    continue
                # If the argument is "created_at" or "updated_at", convert it to a datetime object
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                # Set the argument as an instance variable
                else:
                    self.__dict__[key] = value
    def __str__(self):
        """Return string representation of the class"""
        rep = f"[(self.__class__.__name__)] ({self.id}) {self.__dict__}"
        return rep

    def save(self):
        """Update the updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dict containing all key and value of dict"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

