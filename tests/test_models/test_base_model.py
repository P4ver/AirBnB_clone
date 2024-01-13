#!/usr/bin/python3
"""
Define Unittest,
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unitest.TestCase):
    """
    Unittest tsting inst,
    """
    def test_inst(self):
        self.assertIn(BaseModel(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
