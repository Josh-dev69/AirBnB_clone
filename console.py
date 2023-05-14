#!/usr/bin/env python3
"""
This module contains the HBNBCommand class, which implements
a command interpreter using the cmd module.
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage

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
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
        except NameError:
            print("** class doesn't exist **")
            return
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        
        if key not in objects:
            print("** no instance found **")
            return
        obj = self.objects[key]
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        if key not in self.objects:
            print("** no instance found **")
            return

        del self.objects[key]
        self.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        objects_list = []
        for key, obj in self.objects.items():
            class_name = key.split(".")[0]
            if not arg or arg == class_name:
                objects_list.append(str(obj))
        print(objects_list)

    def update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in self.objects:
            print("** no instance found **")
            return

        obj = self.objects[key]
        if len(args) == 2:
            print(obj)
            return
        elif len(args) == 3:
            print("** attribute name missing **")
            return
        elif len(args) == 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        if isinstance(attribute_value, (str, int, float)):
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        else:
            print("** value must be a string, an integer or a float **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
