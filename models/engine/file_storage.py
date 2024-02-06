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
        tmp = dict()
        for keys in self.__objects.keys():
            tmp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(tmp, jsonfile)

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
            with open(self.__file_path) as jsonfile:
                obj_list = json.load(jsonfile)
            for keys in obj_list.keys():
                if obj_list[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**obj_list[keys])
                elif obj_list[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**obj_list[keys])
