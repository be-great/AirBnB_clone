#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py.
"""
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def testObjectOfFileStorage(self):
        """
        test an object of FileStorage is instance of FileStorage class
        """
        self.assertEqual(type(FileStorage(), FileStorage))

    def testObjectOfFileStorageWithArg(self):
        """
        test an object of FileStorage is instance of FileStorage class with None
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testStorageInistance(self):
        self.assertEqual(type(models.storage), FileStorage)

    def testNewMethod(self):
        """
        test new(self) method
        """
        b1 = BaseModel()
        models.storage.new(b1)
        self.assertIn("BaseModel.{}".format(b1.id), models.storage.all())

    def testAll(self):
        """
        test all method
        """
        self.assertEqual(dict, type(models.storage.all()))

    def testNewMethodWithArgs(self):
        """
        test new method with more  than on args
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def testNewMethodWithNone(self):
        """
        test new method new(None)
        """

        with self.assertRaises(AttributeError):
            models.storage.new(None)
