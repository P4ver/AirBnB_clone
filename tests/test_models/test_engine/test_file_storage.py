#!/usr/bin/python3
"""
Module for flstrge,
"""
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Unittest for Filestorage cls,
    """

    @classmethod
    def setUp(cls):
        cls.file_storage0 = FileStorage()


if __name__ == '__main__':
    unittest.main()
