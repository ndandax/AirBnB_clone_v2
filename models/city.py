#!/usr/bin/python3
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """Representation of city """
     __tablename__ = 'cities'
    state_id = Column(string(60), nullable=False, ForeignKey('states.id'))
    name = Column(string(128), nullable=False)

    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
