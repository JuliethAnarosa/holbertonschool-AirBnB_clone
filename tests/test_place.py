#!/usr/bin/python3
import unittest
from models.place import Place
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
        "city_id": "homo",
        "user_id": "homini",
        "name": "lupus",
        "description": "est",
        "number_rooms": 6,
        "number_bathrooms": 9,
        "max_guest": 40,
        "price_by_night": 10,
        "latitude": 80.0,
        "longitude": 8.9,
        "amenity_ids": ["a", "b", "c"]
    }
    tmp = Place(**kw)
    tmp.save()

    objs = storage.all()

    def test_attributes(self):
        for i in self.kw.keys():
            self.assertEqual(self.kw[i], self.tmp.__dict__[i])