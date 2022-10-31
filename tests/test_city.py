#!/usr/bin/python3
import unittest
from models.city import City
from uuid import uuid4, UUID
from datetime import datetime
from models import storage

def is_valid_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False

class TestBaseModel(unittest.TestCase):
    kw = {
        "state_id": "BA",
        "name": "Barcelona",
    }
    tmp = City(**kw)
    tmp.save()

    objs = storage.all()

    def test_attributes(self):
        a = self.objs[self.tmp.__class__.__name__ + "." + self.tmp.id].to_dict()
        for i in self.kw.keys():
            self.assertEqual(self.kw[i], a[i])