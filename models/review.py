#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class in هnherited from BaseModel class.
    """
    # Initialize public class variables
    place_id = ""
    user_id = ""
    text = ""
