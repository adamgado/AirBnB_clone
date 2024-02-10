#!/usr/bin/python3
"""FileStorage unittests"""
import sys
sys.path.append('../../..')
from datetime import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
import unittest
import uuid


class TestFileStorage(unittest.TestCase):
    """tests for file storage"""

    def test_all(self):
        """test all() method"""
        db_list = FileStorage()
        all_objects = db_list.all()
        self.assertIsNotNone(all_objects)
        self.assertEqual(type(all_objects), dict)
        self.assertIs(all_objects, db_list._FileStorage__objects)

    def test_new(self):
        """test new() method"""
        db_list = FileStorage()
        all_objects = db_list.all()
        obj = BaseModel()
        db_list.new(obj)
        new_obj = obj.__class__.__name__ + "." + str(obj.id)
        self.assertIsNotNone(all_objects[new_obj])

    def test_save(self):
        """test save() method"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        db_list = FileStorage()
        self.assertFalse(os.path.exists('file.json'))
        db_list.save()
        self.assertTrue(os.path.exists('file.json'))
        os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
