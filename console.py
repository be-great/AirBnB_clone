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
    Delete an object from storage by its ID.

    Args:
        id (str): The ID of the object to delete.

    Returns:
        bool or None: True if the object was successfully deleted,\
        None if no object with the specified ID was found.

    Example Usage:
        result = deleteObjectById("1234-5678-9012")
        if result:
            print("Object deleted successfully.")
        elif result is None:
            print("No object found with the specified ID.")
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
    """
    Find an object by its ID.

    Args:
        id (str): The ID of the object to search for.

    Returns:
        obj: The object found with the specified ID, or None\
        if no such object exists.

    Example Usage:
        obj = findObjectById("1234-5678-9012")
        if obj:
            print("Object found:", obj)
        else:
            print("Object not found.")
    """
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
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Add a newline for better formatting
        return True

    def do_create(self, arg):
        """
        Create a new instance of a specified \
        class and save it to the storage.
        """
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
        """Display the string representation of an instance \
        based on the class name"""
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
        """
    Delete an instance of a specified class based on its ID.
    """
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
        Print all string representations of objects or \
        all objects of a specified class.
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
