#!/usr/bin/python3
"""Def a class testHBNBCommand"""
import unittest
import console
import pep8


class TestHBNBCommand(unittest.TestCase):
    """tst class,"""
    def test_p8a(self):
        p8stl = pep8.StyleGuide(quiet=True)
        res = p8stl.check_files(["console.py"])
        self.assertEqual(res.total_errors, 0, "==>> error")

    def test_ds(self):
        self.assertIsNotNone(console.__doc__)


if __name__ == '__main__':
    unittest.main()
