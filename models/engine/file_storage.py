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
        for a in self.__objects.keys():
            db_json[a] = self.__objects[a].to_dict()
        with open(self.__file_path, mode='w') as f:
            json.dump(db_json, f)

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
            with open(self.__file_path) as f:
                db_dict = json.load(f)
            for a in db_dict.keys():
                if db_dict[a]['__class__'] == "BaseModel":
                    self.__objects[a] = BaseModel(**db_dict[a])
                elif db_dict[a]['__class__'] == "User":
                    self.__objects[a] = User(**db_dict[a])
                elif db_dict[a]['__class__'] == "State":
                    self.__objects[a] = State(**db_dict[a])
                elif db_dict[a]['__class__'] == "City":
                    self.__objects[a] = City(**db_dict[a])
                elif db_dict[a]['__class__'] == "Amenity":
                    self.__objects[a] = Amenity(**db_dict[a])
                elif db_dict[a]['__class__'] == "Place":
                    self.__objects[a] = Place(**db_dict[a])
                elif db_dict[a]['__class__'] == "Review":
                    self.__objects[a] = Review(**db_dict[a])
