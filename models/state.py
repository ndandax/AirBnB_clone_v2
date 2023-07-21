#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
<<<<<<< HEAD
    """Representation of state """

    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="states")
    else:
        name = ""

        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            values_city = models.storage.all("City")
            list_city = []
            for city in values_city.values():
=======
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
