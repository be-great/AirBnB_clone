#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py.
"""
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmpfile")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmpfile", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    """Test cases for the FileStorage class."""

    def testObjectOfFileStorage(self):
        """
        test an object of FileStorage is instance of FileStorage class
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def testObjectOfFileStorageWithArg(self):
        """
        test an object of FileStorage is instance of
        FileStorage class with None
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

    def test_reload_instacnce(self):
        basemodel = BaseModel()
        usermodel = User()
        stmodel = State()
        placemodel = Place()
        citymodel = City()
        Amenitymodel = Amenity()
        reviewmodel = Review()
        models.storage.new(basemodel)
        models.storage.new(usermodel)
        models.storage.new(stmodel)
        models.storage.new(placemodel)
        models.storage.new(citymodel)
        models.storage.new(Amenitymodel)
        models.storage.new(reviewmodel)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + basemodel.id, objs)
        self.assertIn("User." + usermodel.id, objs)
        self.assertIn("State." + stmodel.id, objs)
        self.assertIn("Place." + placemodel.id, objs)
        self.assertIn("City." + citymodel.id, objs)
        self.assertIn("Amenity." + Amenitymodel.id, objs)
        self.assertIn("Review." + reviewmodel.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_instacnce(self):
        basemodel = BaseModel()
        usermodel = User()
        stmodel = State()
        placemodel = Place()
        citymodel = City()
        Amenitymodel = Amenity()
        reviewmodel = Review()
        models.storage.new(basemodel)
        models.storage.new(usermodel)
        models.storage.new(stmodel)
        models.storage.new(placemodel)
        models.storage.new(citymodel)
        models.storage.new(Amenitymodel)
        models.storage.new(reviewmodel)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + basemodel.id, save_text)
            self.assertIn("User." + usermodel.id, save_text)
            self.assertIn("State." + stmodel.id, save_text)
            self.assertIn("Place." + placemodel.id, save_text)
            self.assertIn("City." + citymodel.id, save_text)
            self.assertIn("Amenity." + Amenitymodel.id, save_text)
            self.assertIn("Review." + reviewmodel.id, save_text)

    def test_save_instacnce_witharg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_all_instacnce(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_witharg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


if __name__ == '__main__':
    unittest.main()
