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
        