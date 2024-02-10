#!/usr/bin/python3
"""Place unittest"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """tests for Place class"""

    def test_class(self):
        """test class of Place objects"""
        a = Place()
        self.assertIsInstance(a, Place)

    def test_inheritance(self):
        """test Place is subclass of basemodel"""
        a = Place()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = Place()
        self.assertTrue(hasattr(a, "city_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "name"))
        self.assertTrue(hasattr(a, "description"))
        self.assertTrue(hasattr(a, "number_rooms"))
        self.assertTrue(hasattr(a, "number_bathrooms"))
        self.assertTrue(hasattr(a, "max_guest"))
        self.assertTrue(hasattr(a, "price_by_night"))
        self.assertTrue(hasattr(a, "latitude"))
        self.assertTrue(hasattr(a, "longitude"))
        self.assertTrue(hasattr(a, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
