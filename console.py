#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
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
        if len(arguments) < 1 :
            print("** class name missing **")
        elif arguments[0] not in self.__classnames:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
