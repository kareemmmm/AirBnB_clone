#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel instance."""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        parsed_time = datetime.strptime(
                            value, time_format
                        )
                        setattr(self, key, parsed_time)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates updated_at with current datetime and saves storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/values of __dict__."""
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
