#!/usr/bin/python3
import unittest
from models.review import Review
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
        "place_id": "di_ecalp",
        "user_id": "di_resu",
        "text": "txet",
    }
    tmp = Review(**kw)
    tmp.save()

    def test_attributes(self):
        for i in self.kw.keys():
            self.assertEqual(self.kw[i], self.tmp.__dict__[i])