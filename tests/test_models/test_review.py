#!/usr/bin/python3
"""Review unittest"""
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """tests for Review class"""

    def test_class(self):
        """test class of Review objects"""
        a = Review()
        self.assertIsInstance(a, Review)

    def test_inheritance(self):
        """test Review is subclass of basemodel"""
        a = Review()
        self.assertIsInstance(a, BaseModel)

    def test_attribute(self):
        """test attributes"""
        a = Review()
        self.assertTrue(hasattr(a, "place_id"))
        self.assertTrue(hasattr(a, "user_id"))
        self.assertTrue(hasattr(a, "text"))


if __name__ == "__main__":
    unittest.main()
