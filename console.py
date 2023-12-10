#!/usr/bin/python3
"""Entry point of command interpreter module"""


import cmd
from datetime import datetime
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
               'Place', 'Review']

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
            class_name = line.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            model_class = globals()[class_name]
            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)
        except AttributeError:
            print("** class doesn't exist **")

    def parse_line_args(self, line):
        """Parses line arguments and returns class name and instance id"""
        command, arg = self.parseline(line)
        if command == '':
            print("** class name missing **")
            return None, None
        if command not in self.classes:
            print("** class doesn't exist **")
            return None, None
        if arg == '':
            print("** instance id missing **")
            return command, None
        return command, arg

    def common_checks(self, command, arg):
        """Common checks for show, destroy, and update methods"""
        if command is None or arg is None:
            return False
        key = command + '.' + arg
        data = storage.all().get(key)
        if data is None:
            print("** no instance found **")
            return False
        return True

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = line.split()

        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            command = args[0]
            arg = args[1]
            if command not in self.classes:
                print("** class doesn't exist **")
            else:
                key = command + '.' + arg
                data = storage.all().get(key)
                if data is None:
                    print("** no instance found **")
                else:
                    print(data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        args_size = len(args)

        if args_size == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if args_size == 1:
            print("** instance id missing **")
            return

        command, instance_id = args

        key = command + '.' + instance_id
        data = storage.all().pop(key, None)

        if data is None:
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = shlex.split(line)

        if not args or args[0] not in self.classes:
            print("** class name missing **")
            return

        class_name = args[0]
        objs = storage.all()

        if class_name == 'BaseModel' or class_name in self.classes:
            print(
                [
                    str(obj) for obj in objs.values()
                    if isinstance(obj, globals()[class_name])
                ]
            )
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = shlex.split(line)
        args_size = len(args)

        if args_size == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if args_size == 1:
            print("** instance id missing **")
            return

        command, instance_id, *attributes = args

        key = command + '.' + instance_id
        instance_data = storage.all().get(key)

        if instance_data is None:
            print("** no instance found **")
            return

        if len(attributes) < 2:
            print("** attribute name or value missing **")
            return

        attribute_name, value = attributes[0], attributes[1]
        value = self.analyze_parameter_value(value)

        setattr(instance_data, attribute_name, value)
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

    def get_objects(self, instance=''):
        """Gets the elements created by the console

        This method takes care of obtaining the information
        of all the instances created in the file `objects.json`
        that is used as the storage engine.

        When an instance is sent as an argument, the function
        takes care of getting only the instances that match the argument.

        Args:
            instance (:obj:`str`, optional): The instance to finds into
                the objects.

        Returns:
            list: If the `instance` argument is not empty, it will search
            only for objects that match the instance. Otherwise, it will show
            all instances in the file where all objects are stored.

        """
        objects = storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.

        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
