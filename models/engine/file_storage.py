#!/usr/bin/python3
"""This file handles serialization and deserialization"""
import json
import os.path
from models.base_model import BaseModel

class FileStorage:
    """Storage engine for serialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all instances"""
        return self.__objects

    def new(self, obj):
        """Create a new instance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Save an existing instance to the file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Load all instances from the file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                obj = BaseModel.from_dict(value)
                self.__objects[key] = obj
