#!/usr/bin/pyhton3
"""This module defines a class called user"""

from models.base_model import BaseModel


class User(BaseModel):
    '''Defines the content of user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
