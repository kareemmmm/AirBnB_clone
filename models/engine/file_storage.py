#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON and deserializes JSON back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        classes = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val["__class__"]
                    if class_name in classes:
                        self.new(classes[class_name](**val))
        except FileNotFoundError:
            pass
