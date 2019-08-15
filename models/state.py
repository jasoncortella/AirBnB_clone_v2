#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship('City',
                          backref='state')

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            return [x for city in models.storage.all(City)
                    if city.state_id == self.id]
