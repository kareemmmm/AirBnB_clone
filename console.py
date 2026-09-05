#!/usr/bin/python3
"""Defines the HBNBCommand class."""
import cmd
import re
import shlex
import models
from models.base_model import BaseModel

CLASSES = {
    "BaseModel": BaseModel
}


def parse_args(arg):
    """Parse string arguments into a list of arguments using shlex."""
    return shlex.split(arg)


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line entry."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class_name>
        Creates a new instance of BaseModel and saves it to JSON file.
        """
        args = parse_args(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            new_instance = CLASSES[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class_name> <id>
        Prints representation of instance based on class and id.
        """
        args = parse_args(arg)
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            print(objects[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Usage: destroy <class_name> <id>
        Deletes an instance based on class name and id.
        """
        args = parse_args(arg)
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            del objects[f"{args[0]}.{args[1]}"]
            models.storage.save()

    def do_all(self, arg):
        """Usage: all or all <class_name>
        Prints all string representation of instances.
        """
        args = parse_args(arg)
        objects = models.storage.all()
        obj_list = []

        if len(args) > 0 and args[0] not in CLASSES:
            print("** class doesn't exist **")
            return

        for obj in objects.values():
            if len(args) > 0 and args[0] == obj.__class__.__name__:
                obj_list.append(str(obj))
            elif len(args) == 0:
                obj_list.append(str(obj))

        print(obj_list)

    def do_count(self, arg):
        """Usage: count <class_name> or <class_name>.count()
        Retrieves the number of instances of a given class.
        """
        args = parse_args(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return

        count = sum(
            1 for obj in models.storage.all().values()
            if obj.__class__.__name__ == args[0]
        )
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> "<attribute_value>"
        Updates an instance attribute based on class name and id.
        """
        args = parse_args(arg)
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_name in ("id", "created_at", "updated_at"):
            return

        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Handle alternate dot-notation syntax (e.g. BaseModel.all())."""
        match = re.match(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if not match:
            print(f"*** Unknown syntax: {line}")
            return

        cls_name, command, raw_args = match.groups()

        if command == "all":
            self.do_all(cls_name)
        elif command == "count":
            self.do_count(cls_name)
        elif command == "show":
            self.do_show(f"{cls_name} {raw_args.strip('\"\'')}")
        elif command == "destroy":
            self.do_destroy(f"{cls_name} {raw_args.strip('\"\'')}")
        elif command == "update":
            dict_match = re.match(
                r"^[\"']([^\"']+)[\"'],\s*(\{.*\})$", raw_args
            )
            if dict_match:
                inst_id, dict_str = dict_match.groups()
                try:
                    attr_dict = eval(dict_str)
                    if isinstance(attr_dict, dict):
                        for k, v in attr_dict.items():
                            self.do_update(
                                f"{cls_name} {inst_id} {k} \"{v}\""
                            )
                        return
                except Exception:
                    pass

            args = raw_args.split(",")
            if len(args) >= 3:
                inst_id = args[0].strip(" \"'")
                attr_name = args[1].strip(" \"'")
                attr_val = args[2].strip(" \"'")
                self.do_update(
                    f"{cls_name} {inst_id} {attr_name} \"{attr_val}\""
                )
            elif len(args) == 2:
                inst_id = args[0].strip(" \"'")
                attr_name = args[1].strip(" \"'")
                self.do_update(f"{cls_name} {inst_id} {attr_name}")
            elif len(args) == 1 and args[0]:
                inst_id = args[0].strip(" \"'")
                self.do_update(f"{cls_name} {inst_id}")
            else:
                self.do_update(cls_name)
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
