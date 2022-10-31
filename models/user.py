#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self):
        self.updated_at = datetime.now()
        d = self.__dict__
        ds = storage.all()
        ds[self.__class__.__name__ + "." + self.id].__dict__.update(d)
        storage.save()