#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_no_arg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_idtype(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models(self):
        mymodel1 = BaseModel()
        mymodel2 = BaseModel()
        self.assertNotEqual(mymodel1.id, mymodel2.id)

    def test_created_at_with_different_model(self):
        mymodel1 = BaseModel()
        sleep(1)
        mymodel2 = BaseModel()
        self.assertLess(mymodel1.created_at, mymodel2.created_at)

    def test_updated_at_with_different_model(self):
        mymodel1 = BaseModel()
        sleep(1)
        mymodel2 = BaseModel()
        self.assertLess(mymodel1.updated_at, mymodel2.updated_at)

    def test_repr(self):
        date = datetime.today()
        date_repr = repr(date)
        base = BaseModel()
        base.id = "sddfdsf"
        base.created_at = base.updated_at = date
        basestr = base.__str__()
        self.assertIn("[BaseModel] (sddfdsf)", basestr)
        self.assertIn("'id': 'sddfdsf'", basestr)
        self.assertIn("'created_at': " + date_repr, basestr)
        self.assertIn("'updated_at': " + date_repr, basestr)

    def test_args_unused(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        bm = BaseModel(id="fdf", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(bm.id, "fdf")
        self.assertEqual(bm.created_at, date)
        self.assertEqual(bm.updated_at, date)

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        base = BaseModel("12", id="777", created_at=date_iso,
                         updated_at=date_iso)
        self.assertEqual(base.id, "777")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_save(self):
        base = BaseModel()
        sleep(1)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)

    def test_saves(self):
        base = BaseModel()
        sleep(1)
        first_updated_at = base.updated_at
        base.save()
        second_updated_at = base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(1)
        base.save()
        self.assertLess(second_updated_at, base.updated_at)

    def test_with_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_updates_file(self):
        base = BaseModel()
        base.save()
        baseid = "BaseModel." + base.id
        with open("file.json", "r") as f:
            self.assertIn(baseid, f.read())

    def test_to_dicttype(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dictkeys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_contrast_to_dict(self):
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)

    def test_with_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)

    def test_to_dict(self):
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 98
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_to_dict(self):
        date = datetime.today()
        base = BaseModel()
        base.id = "fff"
        base.created_at = base.updated_at = date
        dict_ = {
            'id': 'fff',
            '__class__': 'BaseModel',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(base.to_dict(), dict_)


if __name__ == "__main__":
    unittest.main()
