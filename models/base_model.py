#!/usr/bin/python3
""" The BaseModel class module."""


import uuid
from datetime import datetime
import models


class BaseModel:
    """A class BaseModel that defines all common attributes/methods
    for other classes.

    """
    def __init__(self, *args, **kwargs):
        """Initializing the instances

        Args:
        id: string - assigned with an uuid when an instance is created.
        created_at: datetime - assigned with the current datetime when
                    an instance is created.
        updated_at: datetime - assign with the current datetime when an
                    instance is created and it will be updated every time
                    you change your object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    date_format = '%Y-%m-%dT%H:%M:%S.%f'
                    date_time = datetime.strptime(kwargs[key], date_format)
                    setattr(self, key, date_time)
                    continue
                setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updates the public instance attribute updated_at
        with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
