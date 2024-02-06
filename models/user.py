#!/usr/bin/python3
"""User class inherit from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
