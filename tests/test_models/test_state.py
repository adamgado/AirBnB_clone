#!/usr/bin/python3
"""State unittest"""
import sys
sys.path.append('../..')
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """tests for state class"""

    def test_class(self):
        """test class of state objects"""
        a = State()
        self.assertIsInstance(a, State)

    def test_inheritance(self):
        """test State is subclass of basemodel"""
        a = State()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = State()
        self.assertTrue(hasattr(a, "name"))


if __name__ == "__main__":
    unittest.main()
