#!/usr/bin/python3
"""module that defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
import uuid
from os import getenv

=======
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9

Base = declarative_base()


class BaseModel:
<<<<<<< HEAD
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
=======
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
<<<<<<< HEAD
        if kwargs.get("updated_at"):
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f'
                                                     )
        if kwargs.get("created_at"):
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f'
                                                     )
        if kwargs.get("__class__"):
            del kwargs['__class__']
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict = self.__dict__.copy()
        if "_sa_instance_state" in dict:
            dict.pop("_sa_instance_state")
        return '[{}] ({}) {}'.format(cls, self.id, dict)
=======
        if kwargs:
            dformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, dformat))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop("_sa_instance_state", None)
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, dictionary)
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """returns a dictionary containing all keys/values of the instance"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            dictionary.pop("_sa_instance_state")
        return dictionary

    def delete(self):
        """Delete current instance from storage by calling its delete method"""
        models.storage.delete()
=======
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
