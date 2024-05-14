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
