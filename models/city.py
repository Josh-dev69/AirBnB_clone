#!/usr/bin/python3
""" This module inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Representation of the City Class """
    state_id = ""
    name = ""
