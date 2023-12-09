#!/usr/bin/python3
"""Entry point of command interpreter module"""


import cmd
from datetime import datetime
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = '(hbnb) '
    classes = ['BaseModel']

    def do_EOF(self, line):
        """Handle EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return

        try:
            # Dynamically instantiate the class based on
            # the provided class name
            class_name = line.split()[0]
            new_instance = globals()[class_name]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            data = storage.all().get(command + '.' + arg)
            if data is None:
                print("** no instance found **")
            else:
                print(data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]

        if command is None:
            print("** class name missing **")
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print("** instance id missing **")
        else:
            key = command + '.' + arg
            data = storage.all().get(key)
            if data is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        command = self.parseline(line)[0]
        objs = storage.all()
        if command is None:
            print([str(objs[objs]) for obj in objs])
        elif command in self.classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            instance_data = storage.all().get(key)
            if instance_data is None:
                print("** no instance found **")
            elif args_size == 2:
                print("** attribute name missing **")
            elif args_size == 3:
                print("** value missing **")
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(instance_data, args[2], args[3])
                setattr(instance_data, 'updated_at', datetime.now())
                storage.save()

    def analyze_parameter_value(self, value):
        """Checks a parameter value for an update
        Analyze if a parameter is a string that needs
        convert to a float number or an integer number.

        Args:
            value: The value to analyze
        """
        if value.isdigit():
            return int(value)
        if value.replace(".", "", 1).isdigit():
            return float(value)

        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
