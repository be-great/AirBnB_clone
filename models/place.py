#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    User class in هnherited from BaseModel class.
    """
    # Initialize public class variables
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
