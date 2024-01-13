#!/usr/bin/python3
"""
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unitest.TestCase):
    def test_inst(self):
        self.assertIn(BaseModel(), models.storage.all().values())
