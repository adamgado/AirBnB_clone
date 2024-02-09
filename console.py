#!/usr/bin/python3
"""entry point of the command interpreter"""
from datetime import datetime
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class """
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Quit to exit program"""
        return True

    def do_EOF(self, line):
        """EOF to exit program"""
        return True

    def emptyline(self):
        """empty line + ENTER do nothing"""
        pass

    def do_create(self, *args):
        """create a new instance of class"""
        class_name = args[0]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        else:
            created = eval(class_name)()
            created.save()
            print(created.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
