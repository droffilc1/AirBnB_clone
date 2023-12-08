#!/usr/bin/python3
"""Entry point of command interpreter module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handle EOF"""
        exit()

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
