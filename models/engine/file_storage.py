#!/usr/bin/python3
import json
import os.path
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            objs = dict(self.__objects)
            for k, v in objs.items():
                objs[k] = objs[k].to_dict()
                #print("SAVING")
                #print(objs[k])
            f.write(json.dumps(objs))

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                a = f.read()
                if not a.isspace() and len(a) > 0:
                    d = json.loads(a)
                    #print("DDD")
                    #print(type(d))
                    #print(d)
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            for k, v in d.items():
                d[k] = eval(v["__class__"])(**v)
            #print("NEW DDD")
            #print(d)
            self.__objects.update(d)