#!/usr/bin/env python3
"""
This module contains the HBNBCommand class, which implements
a command interpreter using the cmd module.
"""

import cmd
import sys
from models.user import User

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

    def do_create(self, arg):
        """Create a new User instance, saves it (to the JSON file)
        and prints the id.
        """
        user = User()
        args = arg.split()
        for assignment in args:
            key, value = assignment.split('=')
            if hasattr(user, key):
                setattr(user, key, value)
        user.save()
        print(user.id)

    def do_show(self, arg):
        """Prints the string representation of a User instance based on the
        class name and id.
        """
        self._print_model_instance_by_class_id(User, arg)

    def do_destroy(self, arg):
        """Deletes a User instance based on the class name and id."""
        self._destroy_model_instance_by_class_id(User, arg)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name.
        """
        self._print_all_model_instances_by_class(User)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        self._update_model_instance_by_class_id(User, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
