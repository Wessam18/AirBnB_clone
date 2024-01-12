#!/usr/bin/python3
"""build console for AirBnB site"""
import cmd
import re

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """eof command to exit the program"""
        print()
        return True

    def emptyline(self):
        """do nothing on empty line"""
        pass

    def do_create(self, arg):
        """command create new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in storage.all_classes():
                print("** class doesn't exit **")
            else:
                class_object = storage.all_classes()[class_name]
                new_instance = class_object()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """command print string represetation of an instance"""
        splitted_arg = arg.split()
        if len(splitted_arg) == 0:
            print("** class name missing **")
        elif len(splitted_arg) == 1:
            print("** instance id missing **")
        elif splitted_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            class_id = f"{splitted_arg[0]}.{splitted_arg[1]}"
            if class_id not in storage.all().keys():
                print("** no instance found **")
            else:
                for key, value in storage.all().items():
                    if key == class_id:
                        print(value)

    def do_update(self, arg):
        """command update an instance based on class name and id"""
        splitted_arg = arg.split()
        if len(splitted_arg) == 0:
            print("** class name missing **")
        elif len(splitted_arg) == 1:
            print("** instance id missing **")
        elif len(splitted_arg) == 2:
            print("** attribute name missing **")
        elif len(splitted_arg) == 3:
            print("** value missing **")
        elif splitted_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            class_id = f"{splitted_arg[0]}.{splitted_arg[1]}"
            if class_id not in storage.all().keys():
                print("** no instance found **")
            else:
                if type(splitted_arg[3]) not in [str, int, float]:
                    pass
                else:
                    setattr(storage.all()[class_id], splitted_arg[2], splitted_arg[3])
                    storage.save()

    def do_destroy(self, arg):
        """command deletes an instance based on class name and id"""
        splitted_arg = arg.split()
        if len(splitted_arg) == 0:
            print("** class name missing **")
        elif splitted_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(splitted_arg) == 1:
            print("** instance id missing **")
        else:
            key = f"{splitted_arg[0]}.{splitted_arg[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del(storage.all()[key])
                storage.save()

    def do_all(self, arg):
        """print all str representation of all instances"""
        splitted_arg = arg.split()
        if len(splitted_arg) == 1 and splitted_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            all_instances = []
            for value in storage.all().values():
                if len(splitted_arg) == 1 and splitted_arg[0] == value.__class__.__name__:
                    all_instances.append(str(value))
                elif len(splitted_arg) == 0:
                    all_instances.append(str(value))
            print(all_instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
