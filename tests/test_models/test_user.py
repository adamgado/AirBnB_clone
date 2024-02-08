#!/usr/bin/python3
"""User unittest"""
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """tests for user class"""

    def test_class(self):
        """test class of user objects"""
        a = User()
        self.assertIsInstance(a, User)

    def test_inheritance(self):
        """test user is subclass of basemodel"""
        a = User()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = User()
        self.assertTrue(hasattr(a, "email"))
        self.assertTrue(hasattr(a, "password"))
        self.assertTrue(hasattr(a, "first_name"))
        self.assertTrue(hasattr(a, "last_name"))


if __name__ == "__main__":
    unittest.main()
