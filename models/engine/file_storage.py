from ..base_model import BaseModel


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
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: Object to be added to storage.
            It must have an attribute named 'id'.
        """

        self.__objects[obj.__class__.__name__.id] = obj
