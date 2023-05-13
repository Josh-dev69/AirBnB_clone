#!/usr/bin/env python3
"""
This module contains the HBNBCommand class, which implements
a command interpreter using the cmd module.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class implements a command interpreter using the cmd module.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
