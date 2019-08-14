#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Columnn(String(128), nullable=False)
    last_name = Columnn(String(128), nullable=False)
