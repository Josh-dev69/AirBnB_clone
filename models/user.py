#!/usr/bin/python3
"""Defining the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
