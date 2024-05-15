#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class in هnherited from BaseModel class.
    """
    # Initialize public class variables
    state_id = ""
    name = ""
