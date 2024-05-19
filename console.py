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
import re
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
    id = id.strip('\"\'')

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
        print(parts)
        if len(parts) > 1 or parts[1] not in subcommands:
            classname = parts[0]
            args = parts[1].split("(")
            methodname = args[0]
            extraArg = args[1].split(")")[0]
            allArgs = args[1].split(")")[0].split(",")
            if methodname in subcommands.keys():
                if methodname != "update":
                    return subcommands[methodname]("{} {}".format(classname, extraArg))
                else:
                    idArg = allArgs[0]
                    attrName = allArgs[1]
                    attrValue = allArgs[2]
                    return subcommands[methodname]("{} {} {} {}".format(
                                                                classname,
                                                                idArg,
                                                                attrName,
                                                                attrValue))
        print("*** Unknown syntax: ()".format(parts))
        return False

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
            my_model = deleteObjectById(arguments[1].strip('\"\''))
            if my_model is None:
                print("** no instance found **")

    def do_all(self, arg):
        """
    Print all string representations of objects or all objects of a specified \
    class.

    Args:
        arg (str): The argument passed to the command. If provided, it should \
        contain the class name
                   for which objects need to be printed.

    Returns:
        None

    Prints:
        If the argument is provided and valid (i.e., class name exists):
            - Prints a list of string representations of all objects of the \
            specified class.
        If the argument is not provided or invalid:
            - Prints a list of string representations of all objects across \
            all classes.
            - If the specified class does not exist, prints an error message.

    Example Usage:
        (hbnb) all
            [String representation of all objects across all classes]
        (hbnb) all BaseModel
            [String representation of all objects of class BaseModel]
        (hbnb) all NonExistentClass
            ** class doesn't exist **
    """

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
