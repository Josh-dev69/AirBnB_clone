#!/usr/bin/python3
"""This file handles serialization and deserialization"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Storage engine for serialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all instances"""
        return FileStorage.__objects

    def new(self, obj):
        """Create a new instance"""
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for o in objdict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            return
