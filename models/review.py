#!/usr/bin/python3
"""Defining the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Representation of the Review Class """
    place_id = ""
    user_id = ""
    text = ""
