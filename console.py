#!/usr/bin/python3
"""Defines the HBNBCommand console class."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone project."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return

        instance = CLASSES[args[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            del all_objs[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = shlex.split(arg)
        all_objs = models.storage.all()
        obj_list = []

        if not args:
            for obj in all_objs.values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return

        for key, obj in all_objs.items():
            if key.startswith(args[0] + "."):
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_val = args[3]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_val = attr_type(attr_val)
            except (ValueError, TypeError):
                pass
        else:
            if attr_val.isdigit():
                attr_val = int(attr_val)
            else:
                try:
                    attr_val = float(attr_val)
                except ValueError:
                    pass

        setattr(obj, attr_name, attr_val)
        obj.save()

    def default(self, line):
        """Handles advanced syntax: <class name>.<command>(<args>)."""
        if "." not in line or "(" not in line or not line.endswith(")"):
            return super().default(line)

        try:
            cls_name, rest = line.split(".", 1)
            method, args_str = rest.split("(", 1)
            args_str = args_str.rstrip(")")

            if cls_name not in CLASSES:
                return super().default(line)

            if method == "all":
                return self.do_all(cls_name)

            if method == "count":
                count = 0
                for key in models.storage.all().keys():
                    if key.startswith(cls_name + "."):
                        count += 1
                print(count)
                return

            clean_args = args_str.strip("\"'")

            if method == "show":
                return self.do_show("{} {}".format(cls_name, clean_args))

            if method == "destroy":
                return self.do_destroy("{} {}".format(cls_name, clean_args))

            if method == "update":
                if "{" in args_str and "}" in args_str:
                    id_part, dict_part = args_str.split(",", 1)
                    clean_id = id_part.strip("\"' ")
                    try:
                        eval_dict = eval(dict_part.strip())
                        if isinstance(eval_dict, dict):
                            for k, v in eval_dict.items():
                                self.do_update("{} {} {} {}".format(
                                    cls_name, clean_id, k, str(v)
                                ))
                            return
                    except Exception:
                        pass

                parts = [p.strip("\"' ") for p in args_str.split(",")]
                if len(parts) >= 3:
                    return self.do_update("{} {} {} {}".format(
                        cls_name, parts[0], parts[1], parts[2]
                    ))
                elif len(parts) == 2:
                    return self.do_update("{} {} {}".format(
                        cls_name, parts[0], parts[1]
                    ))
                elif len(parts) == 1:
                    return self.do_update("{} {}".format(
                        cls_name, parts[0]
                    ))

        except Exception:
            pass

        return super().default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
