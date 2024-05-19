#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


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
        serialized_objs = {key: value.to_dict() for key, value
                           in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects:
        - Reads file.json and converts its content to objects
        - Calls self.new() to add each object to the __objects dictionary
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                content = json.load(f)
                for k, v in content.items():
                    class_name = v["__class__"]
                    # Reconstruct the object
                    class_obj = eval(class_name)(**v)
                    self.new(class_obj)
        except FileNotFoundError:
            # If the file doesn't exist, just return
            return

    # Error: fixed the indentation
