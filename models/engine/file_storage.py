#!/usr/bin/python3
"""FileStorage class"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for file storage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """add new object to the __objects dictionary"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """convert and write __objects to json file"""
        db_json = dict()
        for a, b in self.__objects.items():
            db_json[a] = b.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(db_json))

    def reload(self):
        """convert the json file back to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                db_dict = json.loads(f.read())
                for a, b in db_dict.items():
                    self.__objects[a] = eval(b['__class__'])(**b)
