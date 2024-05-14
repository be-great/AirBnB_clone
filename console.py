#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import json
from models.base_model import BaseModel


# read the file
def findobjectbyid(id):
    """
    read file.json file
    """
    try:
        with open("file.json", "r") as f:
            content = json.load(f)
            for k, v in content.items():
                # get the class name
                if id == v["id"]:
                    return eval(v["__class__"] + "(**v)")
    except FileNotFoundError:
        return None


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    """

    prompt = '(hbnb) '
    __classnames = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        arguments = arg.split()
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()

    def do_show(self, arg):
        arguments = arg.split()
        # search the id
        if len(arguments) < 1:
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            my_model = findobjectbyid(arguments[1])
            if my_model is None:
                print("** no instance found **")
            else:
                print(my_model)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
