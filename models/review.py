#!/usr/bin/python3
"""Defining the class Review"""
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
