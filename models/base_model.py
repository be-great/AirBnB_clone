#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes:
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    The BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        *args, **kwargs arguments for the constructor of a BaseModel
        """
        if kwargs:
            # Iterate through kwargs
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()  # I think this doesn't\
            # need to exist in the requirement: otherwise:\
            # create id and created_at as you did previously (new instance)
            models.storage.new(self)

    def __str__(self):
        """str represention of the class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at"""
        """with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        """of __dict__ of the instance: """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
