#!/usr/bin/python3
"""
module serial & deserial,
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Filestorage cls, (serial/deserial)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dict __obj,"""
        return FileStorage.__objects

    def new(self, obj):
        """the key in __obj,"""
        key_o = f"{self.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key_o] = obj

    def save(self):
        """serial __obj to json"""
        dict_o = {}
        for kp in FileStorage.__objects.keys():
            dict_o[kp] = FileStorage.__objects[kp].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as js_fl:
            json.dump(dict_o, js_fl)

    def reload(self):
        """deserial json to __obj,"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as n_fl:
                return json.load(n_fl)
        except Exception:
            pass
