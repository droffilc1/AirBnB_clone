#!/usr/bin/python3
""" file_storage module """

from json.decoder import JSONDecodeError
from ..base_model import BaseModel
import os.path
import json

class FileStorage:
    """Serializes instnces to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path: path to the JSON file
        __objects: stores objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if os.path.exists(FileStorage.__file_path):
                try:
                    with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                        for key, value in json.loads(file.read()).items():
                            obj = eval(value['__class__'])(**value)
                            FileStorage.__objects[key] = obj
                except JSONDecodeError as e:
                    print(f"JSONDecodeError Error: {e}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
