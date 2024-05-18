#!/usr/bin/python3
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

<<<<<<< HEAD
=======
    def default(self, arg):
        subcommands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count}
        # This way is easer than old way
        # How it's work:
        # A dictionary mapping subcommand names to their corresponding methods
        # Call the corresponding method from the subcommands dictionary,
        # passing the classname as an argument

        parts = arg.split(".")
        if len(parts) > 1:
            classname = parts[0]
            methodname = parts[1].split("(")[0]
            idArg = parts[1].split("(")[1].split(")")[0] ## The problem is this method not work if id number inside "" and work without "" try it
            if methodname in subcommands.keys():
                return subcommands[methodname](f"{classname} {idArg}")
        print("*** Unknown syntax: ()".format(parts))
        return False

>>>>>>> 4fe3d6421388159874e6ca4896fc705f7044321c
    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Add a newline for better formatting
        return True

    def do_create(self, arg):
        arguments = arg.split()
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        else:
            obj = eval(arguments[0])()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        arguments = arg.split()
        # search the id
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            my_model = findObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")
            else:
                print(my_model)

    def do_destroy(self, arg):
        arguments = arg.split()
        # search the id
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            # delete the my_model
            my_model = deleteObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")

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

    def do_update(self, arg):
        arguments = arg.split()
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            my_model = findObjectById(arguments[1])
            if my_model is None:
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    if (obj.to_dict())["id"] == arguments[1]:
                        setattr(obj, arguments[2], arguments[3][1:-1])
                        obj.save()

    def do_count(self, arg):
        countOfInstances = 0
        arguments = arg.split()
        if arguments:
            if arguments[0] not in self.__classnames:
                # if class name passed but not exist
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                for obj_class in all_objs.keys():
                    obj = all_objs[obj_class]
                    # Check if the object's class matches the specified class
                    if (obj.to_dict())["__class__"] == arguments[0]:
                        countOfInstances += 1  # Increment the counter if their
                        # class matches
                print(countOfInstances)
        else:
            # If no class name passed
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
