#!/usr/bin/python3
"""Define cls user,"""
from models.base_model import BaseModel


class User(BaseModel):
    """cls for usr,"""
    email = ""
    passwrd = ""
    first_name = ""
    last_name = ""
