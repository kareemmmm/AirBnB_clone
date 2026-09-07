#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review in the AirBnB system."""

    place_id = ""
    user_id = ""
    text = ""
