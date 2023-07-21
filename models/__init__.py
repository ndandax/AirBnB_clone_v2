#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
import os immport getenv
=======
"""This module allows to change the storage type"""
from os import getenv
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
