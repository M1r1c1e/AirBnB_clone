#!/usr/bin/python3
"""Implementing the command line interpreter using Cmd
arg = argument argg = list of split argument
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):

    __classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Prompt to exit the program
        """
        return True

    def emptyline(self):
        return True

    def do_create(self, arg):
        argg = arg.split()

        if len(argg) == 0:
            print("** class name missing **")

        elif argg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            cls_instance = eval(f"{argg[0]}")()
            cls_instance.save()
            print(cls_instance.id)

"""executes show command
"""
    def do_show(self, arg):
        argg = arg.split()

        if len(argg) == 0:
            print("** class name missing **")

        elif argg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argg) == 1:
            print("** instance id missing **")
        elif f"{argg[0]}.{argg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{argg[0]}.{argg[1]}"])

"""executes destroy command
"""
    def do_destroy(self, arg):
        argg = arg.split()

        if len(argg) == 0:
            print("** class name missing **")

        elif argg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argg) == 1:
            print("** instance id missing **")
        elif f"{argg[0]}.{argg[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del (storage.all()[f"{argg[0]}.{argg[1]}"])
        storage.save()

"""print all class using all command
"""
    def do_all(self,arg):
        argg = arg.split()

        if len(argg) == 0:
            print([str(value) for value in storage.all().values()])
        elif argg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(value)for key, value in storage.all().items()if key.startswith(argg[0])])

"""executes update command
"""
    def do_update(self, arg):
        argg = arg.split()
        if len(argg) == 0:
            print("** class name missing **")
        elif argg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(argg) == 1:
            print("** instance id missing **")
        elif len(argg) == 2:
            print("** attribute name missing **")
        elif len(argg) == 3:
            print("** value missing **")
        else:
            obj_key = f'{argg[0]}.{argg[1]}'
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[obj_key]
                try:
                    setattr(obj, argg[2], eval(argg[3]))
                except NameError:
                    setattr(obj, argg[2], argg[3])
                obj.save()

"""execut default command
"""
    def default(self, arg):
        argg = arg.split('.')
        if argg[0] in self.__classes:
            if argg[1] == "all()":
                self.do_all(argg[0])
            elif argg[1] == "count()":
                count = 0
                for key in storage.all():
                    if key.startswith(argg[0]):
                        count += 1
                print(count)
            elif argg[1].startswith("show"):
                uuid = eval(argg[1].strip("show()"))
                self.do_show(f"{argg[0]} {uuid}")
            elif argg[1].startswith("destroy"):
                uuid = eval(argg[1].strip("destroy()"))
                self.do_destroy(f"{argg[0]} {uuid}")
            elif argg[1].startswith("update"):
                if argg[1].endswith("})"):
                    entry = argg[1].strip("update()").strip("}").split(", {")
                    uuid = eval(entry[0])
                    dict = eval('{' + entry[1] + '}')
                    for name, value in dict.items():
                        self.do_update(f"{argg[0]} {uuid} {name} {value}")
                else:
                    entry = argg[1].strip("update()").split(", ")
                    uuid = eval(entry[0])
                    name = eval(entry[1])
                    value = entry[2]
                    self.do_update(f"{argg[0]} {uuid} {name} {value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

