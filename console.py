#!/usr/bin/python3
"""build console for AirBnB site"""
import cmd
import re
import sys
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

    com_classes = ['create', 'show', 'update', 'all', 'destroy', 'count']

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
                print("** class doesn't exist **")
            else:
                class_object = storage.all_classes()[class_name]
                new_instance = class_object()
                storage.save()
                print(new_instance.id)

    def do_show(self, arg):
        """command print string represetation of an instance"""
        splitted_arg = arg.split()
        if len(splitted_arg) == 0:
            print("** class name missing **")
        elif splitted_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(splitted_arg) == 1:
            print("** instance id missing **")
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
        s_arg = arg.split()
        if len(s_arg) == 0:
            print("** class name missing **")
        elif s_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(s_arg) == 1:
            print("** instance id missing **")
        elif f"{s_arg[0]}.{s_arg[1]}" not in storage.all().keys():
            print("** no instance found **")
        elif len(s_arg) == 2:
            print("** attribute name missing **")
        elif len(s_arg) == 3:
            print("** value missing **")
        else:
            key = f"{s_arg[0]}.{s_arg[1]}"

            if type(s_arg[3]) not in [str, float, int]:
                pass
            elif s_arg[2] in ["id", "created_at", "updated_at"]:
                pass
            else:
                value = s_arg[3]
                # check if the value has " char
                if not re.search('"', value):
                    value = s_arg[3]
                else:
                    value = s_arg[3].replace('"', '')

                setattr(storage.all()[key], s_arg[2], value)
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
                del (storage.all()[key])
                storage.save()

    def do_all(self, arg):
        """print all str representation of all instances"""
        s_arg = arg.split()

        if len(s_arg) == 1 and s_arg[0] not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            all_instances = []
            for value in storage.all().values():
                if len(s_arg) == 1 and s_arg[0] == value.__class__.__name__:
                    all_instances.append(str(value))
                elif len(s_arg) == 0:
                    all_instances.append(str(value))
            print(all_instances)

    def do_count(self, arg):
        """function that making count"""
        count = 0
        args = arg.split()

        if args[0] not in storage.all_classes():
            print("class dosen't exist")

        for key, value in storage.all().items():
            class_name = value.__class__.__name__
            if args[0] == class_name:
                count += 1
        print(count)

    def precmd(self, arg):
        """Function That excute before cmd"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls_name = arg.split('.')[0]
            command = arg.split('.')[1].split('(')[0]

            if len(arg.split('.')[1].split('(')[1].split(')')) == 2:
                the_id = arg.split('.')[1].split('(')[1]. \
                        split(')')[0].strip('"')

            if command in HBNBCommand.com_classes and \
                    cls_name in storage.all_classes():
                arg = f"{command} {cls_name} {the_id}"

        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
