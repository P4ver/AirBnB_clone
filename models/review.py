#!/usr/bin/python3
"""
mdl Rview
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reprsent an amenty,
    """
    place_id = ""
    user_id = ""
    text = ""
