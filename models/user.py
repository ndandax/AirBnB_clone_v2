#!/usr/bin/python3
""" holds class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", passive_deletes=True, backref="user")
        reviews = relationship("Review", passive_deletes=True, backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
