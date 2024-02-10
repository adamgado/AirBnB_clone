#!/usr/bin/python3
"""City unittest"""
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """tests for City class"""

    def test_class(self):
        """test class of City objects"""
        a = City()
        self.assertIsInstance(a, City)

    def test_inheritance(self):
        """test City is subclass of basemodel"""
        a = City()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = City()
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "state_id"))


if __name__ == "__main__":
    unittest.main()
