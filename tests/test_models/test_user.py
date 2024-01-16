#!/usr/bin/python3
"""Define unittest"""
import models
import unittest
from models.user import User


class TestUser_inst(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(User, type(User())


if __name__ == "__main__":
    unittest.main()
