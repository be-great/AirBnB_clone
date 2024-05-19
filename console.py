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
        """
    Execute the appropriate method based on the subcommand specified in the \
    argument.

    Args:
        arg (str): The argument passed to the command, which may \
        contain a subcommand
                   and additional parameters separated by dots and parentheses.

    Returns:
        bool: True if the method corresponding to the subcommand \
        is executed successfully,
              False otherwise.

    Prints:
        - If the subcommand is not recognized:
            Prints an error message indicating unknown syntax.

    Example Usage:
        (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            [Output of the show method for the specified User instance]
        (hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", \
        {'first_name': "John", "age": 89})
            [Output of the update method for the specified User instance]
    """
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
                    return subcommands[methodname]("{} {}".format(classname,
                                                                  extraArg))
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
        """
    Display the string representation of an instance based on the class name \
    and ID.

    Args:
        arg (str): The argument passed to the command, which should contain \
        the class name
                   and the ID of the instance separated by a space.

    Returns:
        None

    Prints:
        - If the class name is missing:
            Prints an error message indicating that the class name is missing.
        - If the specified class does not exist:
            Prints an error message indicating that the class does not exist.
        - If the instance ID is missing:
            Prints an error message indicating that the instance ID is missing.
        - If the instance with the specified ID does not exist:
            Prints an error message indicating that no instance was found with \
            that ID.
        - If the instance with the specified ID exists:
            Prints the string representation of the instance.

    Example Usage:
        (hbnb) show
            ** class name missing **
        (hbnb) show BaseModel
            ** instance id missing **
        (hbnb) show BaseModel 123
            ** no instance found **
        (hbnb) show BaseModel 12345-6789-1011
            [String representation of the instance with ID 12345-6789-1011]
    """
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
        """
    Retrieve all instances or instances of a specific class.

    Args:
        arg (str): The argument passed to the command. If provided, it should \
        contain
                   the name of the class for which instances need to be \
                   retrieved.

    Returns:
        None

    Prints:
        - If the argument is provided and valid (i.e., class name exists):
            Prints a list of string representations of instances of the \
            specified class.
        - If no argument is provided:
            Prints a list of string representations of all instances across \
            all classes.
        - If the specified class does not exist:
            Prints an error message indicating that the class does not exist.

    Example Usage:
        (hbnb) all
            [List of string representations of all instances]
        (hbnb) all BaseModel
            [List of string representations of instances of BaseModel]
        (hbnb) all NonExistentClass
            ** class doesn't exist **
    """
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
        """
    Count the number of instances of a specified class.

    Args:
        arg (str): The argument passed to the command. Should contain the name\
                                                         of the class
                   for which instances need to be counted.

    Returns:
        None

    Prints:
        If the argument is provided and valid (i.e., class name exists):
            - Prints the number of instances of the specified class.
        If the argument is not provided:
            - Prints an error message indicating that the class name is\
            missing.
        If the specified class does not exist:
            - Prints an error message indicating that the class does not exist.

    Example Usage:
        (hbnb) count
            ** class name missing **
        (hbnb) count BaseModel
            [Number of instances of BaseModel]
        (hbnb) count NonExistentClass
            ** class doesn't exist **
    """
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
