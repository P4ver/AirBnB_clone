#!/usr/bin/python3
"""
Define Unittest,
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Unittest tsting inst,
    """
    def test_inst(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel.id))


if __name__ == "__main__":
    unittest.main()
