#!/usr/bin/python3
"""
Module for flstrge,
"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittes.TestCase):
    """
    Unittest for Filestorage cls,
    """
    def test_inst(self):
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == "__main__":
    unittest.main()
