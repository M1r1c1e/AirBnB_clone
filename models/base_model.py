#!/usr/bin/python3
import uuid
from datetime import datetime
import models  # Assuming this is your own module

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializing a new instance of BaseModel.

        Args:
            *args: tuple argument list.
            **kwargs: A dictionary arguments.
        """
        if kwargs is not None and len(kwargs) != 0:
            for dic_key, dic_value in kwargs.items():
                if dic_key == "__class__":
                    continue
                elif dic_key == "created_at" or dic_key == "updated_at":
                    self.__dict__[dic_key] = datetime.fromisoformat(dic_value)
                else:
                    self.__dict__[dic_key] = dic_value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        printing string representation of the BaseModel instance.

        Returns:
            str: String representation of basemodel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute and stores the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        convert data gotten of the BaseModel instance to dictionay

        Returns:
            dict: Dictionary representation which begins the convertion to json.
        """
        copied_dict = self.__dict__.copy()
        copied_dict["__class__"] = self.__class__.__name__
        copied_dict["created_at"] = self.created_at.isoformat()
        copied_dict["updated_at"] = self.updated_at.isoformat()
        return copied_dict

