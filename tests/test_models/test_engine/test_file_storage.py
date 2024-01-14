#!/usr/bin/python3
"""

"""
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_inst(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_fil(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_obj(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

if __name__ == '__main__':
    unittest.main()
