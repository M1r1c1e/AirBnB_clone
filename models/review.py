#!/usr/bin/pyhton3
"""This module defines a class called Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    '''Defines what Review consist of'''
    place_id = ""
    user_id = ""
    text = ""
