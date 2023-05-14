#!/usr/bin/python3
"""Defining a file storage class that handles serialization
and deserialization"""
from models.base_model import BaseModel


class FileStorage:
    """serialiazation and deserialization of instance to a json file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self__objects[key] = obj


