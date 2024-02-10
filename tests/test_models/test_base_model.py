#!/usr/bin/python3
"""Unittest for BaseModel"""
import sys
sys.path.append('../..')
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import os
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """tests for base model"""

    def test_class(self):
        """test if object is instance of BaseModel"""
        a = BaseModel()
        self.assertTrue(isinstance(a, BaseModel))

    def test_string_id(self):
        """id is converted to string from uuid"""
        a = BaseModel()
        self.assertIsInstance(a.id, str)

    def test_uuid_good(self):
        """test id is uuid"""
        a = BaseModel()
        self.assertIsInstance(uuid.UUID(a.id), uuid.UUID)

    def test_id_error(self):
        """test id error"""
        a = BaseModel()
        a.id = 'error case'
        err = 'badly formed hexadecimal UUID string'
        with self.assertRaises(ValueError) as e:
            uuid.UUID(a.id)
        self.assertEqual(err, str(e.exception))

    def test_base_model_uuid_version(self):
        """test version of uuid"""
        a = BaseModel()
        id_uuid = uuid.UUID(a.id)
        self.assertEqual(id_uuid.version, 4)

    def test_base_model_different_uuid(self):
        """test id is different per object"""
        a = BaseModel()
        b = BaseModel()
        id_uuid1 = uuid.UUID(a.id)
        id_uuid2 = uuid.UUID(b.id)
        self.assertNotEqual(id_uuid1, id_uuid2)

    def test_datetime_createdat(self):
        """test if created_at is assigned from datetime"""
        a = BaseModel()
        self.assertIsInstance(a.created_at, datetime)

    def test_datetime_updatedat(self):
        """test if updated_at is assigned from datetime"""
        a = BaseModel()
        self.assertIsInstance(a.updated_at, datetime)

    def test_dictionary(self):
        """test dictionary argument attributes"""
        t = datetime.now()
        dic = {"id": "22b5f0bd-99f1-466c-accd-ea3b3ce7c46c", "created_at":
               "2000-01-10T12:30:30.555555", "updated_at":
               "2000-01-10T12:30:30.555555", "__class__": "BaseModel"}
        a = BaseModel(**dic)
        self.assertEqual(a.__class__.__name__, "BaseModel")
        self.assertEqual(a.id, "22b5f0bd-99f1-466c-accd-ea3b3ce7c46c")
        self.assertEqual(type(a.created_at), type(t))
        self.assertEqual(type(a.updated_at), type(t))

    def test_dictionary_add_attributes(self):
        """test dictionary argument with more attributes"""
        t = datetime.now()
        dic = {"id": "22b5f0bd-99f1-466c-accd-ea3b3ce7c46c", "created_at":
               "2000-01-10T12:30:30.555555", "updated_at":
               "2000-01-10T12:30:30.555555", "__class__": "BaseModel",
               "notes": "none", "address": "25th street"}
        a = BaseModel(**dic)
        self.assertEqual(a.__class__.__name__, "BaseModel")
        self.assertEqual(a.id, "22b5f0bd-99f1-466c-accd-ea3b3ce7c46c")
        self.assertEqual(type(a.created_at), type(t))
        self.assertEqual(type(a.updated_at), type(t))
        self.assertEqual(a.notes, "none")
        self.assertEqual(a.address, "25th street")

    def test_attributes(self):
        """test attributes"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_methods(self):
        """test methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_todict(self):
        """test to_dict return"""
        obj = BaseModel()
        obj_dict = obj.__dict__.copy()
        obj_dict["__class__"] = obj.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        created_dict = obj.to_dict()
        self.assertDictEqual(obj_dict, created_dict)

    def test_to_dict_type(self):
        """test to_dict method types"""
        obj = BaseModel()
        base_dict = obj.to_dict()
        self.assertEqual(obj.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_save(self):
        """test save() method"""
        a = BaseModel()
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)


if __name__ == "__main__":
    unittest.main()
