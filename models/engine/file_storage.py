from test import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        