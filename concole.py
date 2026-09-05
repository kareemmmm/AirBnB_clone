#!/usr/bin/python3
"""Defines HBNBCommand, the entry point of the command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty input line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Create a new instance of a class, save it, and print its id.

        Usage: create <class name>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Print all string representations of instances.

        Usage: all [class name]
        """
        args = shlex.split(line)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return
        result = []
        for obj in storage.all().values():
            if len(args) == 0 or type(obj).__name__ == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, line):
        """Update an instance by adding or updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
