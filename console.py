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

    def do_create(self, arg):
        """create a new instance of class"""
        class_name = self.parseline(arg)[0]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        else:
            created = eval(class_name)()
            created.save()
            print(created.id)

    def do_show(self, arg):
        """print string form of object"""
        class_name = self.parseline(arg)[0]
        obj_id = self.parseline(arg)[1]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        elif obj_id == '':
            print('** instance id missing **')
        else:
            found_obj = models.storage.all().get(class_name + '.' + obj_id)
            if found_obj is None:
                print('** no instance found **')
            else:
                print(found_obj)

    def do_destroy(self, arg):
        """delete object from storage"""
        class_name = self.parseline(arg)[0]
        obj_id = self.parseline(arg)[1]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        elif obj_id == '':
            print('** instance id missing **')
        else:
            found_obj = models.storage.all().get(class_name + '.' + obj_id)
            if found_obj is None:
                print('** no instance found **')
            else:
                del models.storage.all()[class_name + '.' + obj_id]
                models.storage.save()

    def do_all(self, arg):
        """print string form of all objects"""
        db_list = models.storage.all()
        class_name = self.parseline(arg)[0]
        if class_name is None:
            for a in db_list:
                print(str(db_list[a]))
        elif class_name not in self.class_list:
            print("** class doesn't exist **")
        else:
            obj_list = db_list.keys()
            for b in obj_list:
                if b.startswith(class_name):
                    print([str(db_list[b])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
