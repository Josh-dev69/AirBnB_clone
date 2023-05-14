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

    def save(self):
        """ Serialize __objects to JSON file """
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """ Deserialize the JSON file to __object """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
