#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_o = f"{self.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key_o] = obj

    def save(self):
        dict_o = {}
        for kp in FileStorage.__objects.keys():
            dict_o[kp] = FileStorage.__objects[kp].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as js_fl:
            json.dump(dict_o, js_fl)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as n_fl:
                return json.load(n_fl)
        except Exception:
            pass
