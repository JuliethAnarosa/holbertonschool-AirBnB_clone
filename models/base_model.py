#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from datetime import date
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k in kwargs.keys():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        fmt = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[k] = datetime.strptime(kwargs[k], fmt)
                    else:
                        self.__dict__[k] = kwargs[k]
        
        storage.new(self)

    def __str__(self):
        name = self.__class__.__name__
        d = dict(self.__dict__)
        d["__class__"] = name
        return "[{}] ({}) {}".format(name, self.id, d)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        d = dict(self.__dict__)
        d["__class__"] = self.__class__.__name__
        d["created_at"] = d["created_at"].isoformat()
        d["updated_at"] = d["updated_at"].isoformat()
        return d