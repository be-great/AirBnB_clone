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
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.loads(f.read())
        except FileNotFoundError:
            return
    # end def
