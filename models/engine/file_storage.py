#!/usr/bin/python3
"""Defines the FileStorage class."""


from models.base_model import BaseModel
import json

class FileStorage:
    """
    This class provides functionality for storing and retrieving objects
    using a file-based storage system. Objects are stored in a dictionary
    format and serialized to a JSON file for persistence across program
    executions.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: Object to be added to storage.
            It must have an attribute named 'id'.
        """

        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj
    def save(self):
        """
        Serializes __objects to JSON file.
        """
        serialized_objs = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objs, file)


    def reload(self):
        """
        deserializes the JSON file to __objects :
        - file.json => BaseModel(args) => self.new()
        - convert the loaded json to BaseModel(args) object to call self.new to add to the __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                content = json.load(f)
                for k, v in content.items():
                    # get the class name
                    classn = v["__class__"]
                    # delete the __class__ attribute becasue it going to created in self.new
                    del v["__class__"]
                    # eval and **v to excute as: classname(**v)
                    my_model = eval(classn)(**v)
                    self.new(my_model)
        except FileNotFoundError:
            return    
    # end def
