#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
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
    tmp = BaseModel()
    tmp.save()

    tmp2 = BaseModel()
    tmp2.save()

    objs = storage.all()

    def test_saved(self):
        k = self.tmp.__class__.__name__ + "." + self.tmp.id
        self.assertTrue(k in self.objs.keys())

    def test_to_dict(self):
        d1 = self.tmp.to_dict()
        d2 = dict(self.tmp.__dict__)
        d2["__class__"] = self.tmp.__class__.__name__
        d2["created_at"] = d2["created_at"].isoformat()
        d2["updated_at"] = d2["updated_at"].isoformat()
        self.assertEqual(d1, d2)

    def test_id(self):
        self.assertTrue(is_valid_uuid(self.tmp2.id))

    def test_created_at(self):
        self.assertTrue(self.tmp.created_at < datetime.now())

    def test_str(self):
        name = self.tmp.__class__.__name__
        d = dict(self.tmp.__dict__)
        d["__class__"] = name
        s = "[{}] ({}) {}".format(name, self.tmp.id, d)
        self.assertEqual(s, self.tmp.__str__())