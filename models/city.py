#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from os import getenv
import sqlalchemy
=======
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """Representation of city """

    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
=======
    """The city class, contains state ID and name"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade="delete", backref="cities")
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
