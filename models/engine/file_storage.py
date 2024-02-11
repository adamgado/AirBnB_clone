#!/usr/bin/python3
"""FileStorage class"""
import json
from os.path import exists


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
        with open(self.__file_path, mode='w') as f:
            f.write(json.dumps(db_json))

    def reload(self):
        """convert the json file back to __objects"""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path, mode='r') as f:
                db_dict = json.loads(f)
                for a, b in db_dict.items():
                    self.__objects[a] = eval(['__class__'])(**b)
