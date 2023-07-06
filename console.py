#!/usr/bin/python3
"""Import modules cmd and BaseModel class"""
import cmd
from models.base_model import BaseModel
"""Console for AirBnB clone"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    file = None

    def do_quit(self, arg):
        """Quits the program with prompt 'quit'"""
        return True

    def help_quit(self):
        """Help string for do_quit method"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Quits the program with prompt 'EOF'(ctrl + D)"""
        return True

    def help_EOF(self):
        """Help string for do_EOF method"""
        print("EOF command to exit the program\n")

    def do_help(self, arg):
        """Prints a help string for each command with prompt 'help'.
        If help + <command>, the method help_<command> executes
        Otherwise, a list of possible commands is displayed"""
        cmd.Cmd.do_help(self, arg)

    def help_help(self):
        """Help string for do_help method"""
        print("Help command to get help about other commands\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
