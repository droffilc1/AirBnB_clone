#!/usr/bin/python3
""" file_storage module """

import os.path
import json
from json.decoder import JSONDecodeError
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    """Serializes instnces to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path: path to the JSON file
        __objects: stores objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                  'City': City, 'Amenity': Amenity, 'Place': Place,
                  'Review': Review}

    def all(self):
        """Returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if os.path.exists(self.__file_path):
                try:
                    with open(self.__file_path, 'r', encoding='utf-8')\
                            as file:
                        obj_dict = json.load(file)
                        for key, value in obj_dict.items():
                            obj, obj_id = key.split(".")
                            self.__objects[key] = globals()[obj](**value)
                except JSONDecodeError:
                    pass
        except FileNotFoundError:
            pass
