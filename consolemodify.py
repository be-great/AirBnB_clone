#!/usr/bin/python3.9
"""Defines the HBnB console."""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models import storage


def deleteObjectById(id):
    """
    delete from file.json
    """
    all_objs = storage.all()
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        if (obj.to_dict())["id"] == id:
            del all_objs[obj_id]
            storage.save()
            return True
    return None


def findObjectById(id):
    all_objs = storage.all()
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        if (obj.to_dict())["id"] == id:
            return obj
    return None
# # read the file
# def findObjectById(id):
#     """
#     read file.json file
#     """
#     try:
#         with open("file.json", "r") as f:
#             content = json.load(f)
#             for k, v in content.items():
#                 # get the class name
#                 if id == v["id"]:
#                     return eval(v["__class__"] + "(**v)")
#     except FileNotFoundError:
#         return None

class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    """

    prompt = '(hbnb) '
    __classnames = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Amenity",
                    "Place",
                    "Review"
                    ]


    def default(self, arg):
        subcommands = ["all",
                       "count"]
        parts = arg.split(".")
        if len(parts) > 1:
            classname = parts[0]
            methodname = parts[1][:-2]
            if methodname in subcommands:
                function = f'self.do_{methodname}("{classname}")'
                eval(function)



    def do_all(self, arg):
        arguments = arg.split()
        list = []
        if len(arguments) >= 1:
            if arguments[0] not in self.__classnames:
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if (obj.to_dict())["__class__"] == arguments[0]:
                        list.append(str(obj))
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                list.append(str(obj))
        print(list)

    def do_count(self, arg):
        arguments = arg.split()
        list = []
        if arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if (obj.to_dict())["__class__"] == arguments[0]:
                    list.append(str(obj))
        print(len(list))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
