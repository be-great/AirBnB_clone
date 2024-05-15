#!/usr/bin/python3
"""Defines the city class."""
from models.base_model import BaseModel


class city(BaseModel):
    """
    city class in inherited from BaseModel class.
    """
    # Initialize public class variables
    state_id = ""
    name = ""
