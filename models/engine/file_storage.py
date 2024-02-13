#!/usr/bin/python3
"""
This module shows how the File Storage class serializes and deserializes
instances to JSON file.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ here obj is the key of __objects which is <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ shows Serializes __objects to the JSON file (path: __file_path) """
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(dic, file)

    def reload(self):
        """ Deserializing the JSON file to __objects (only if the JSON file exists) """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                py_dict = json.load(file)
                for key, value in py_dict.items():
                    clsid = key.split(".")
                    self.__objects[key] = self.__class_dict[clsid[0]](**value)
        except FileNotFoundError:
            pass

