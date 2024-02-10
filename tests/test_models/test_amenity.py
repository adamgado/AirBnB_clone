#!/usr/bin/python3
"""Amenity unittest"""
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """tests for Amenity class"""

    def test_class(self):
        """test class of Amenity objects"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_inheritance(self):
        """test Amenity is subclass of basemodel"""
        a = Amenity()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))


if __name__ == "__main__":
    unittest.main()
