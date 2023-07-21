#!/usr/bin/python3
<<<<<<< HEAD
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates a folder (versions)
    Creates the archive and compresses it into the versions folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".

              format(time))
        return ("versions/web_static_{}.tgz".format(time))
    except Exception:
        return None
=======
"""script that generates a .tgz archive
from the contents of the web_static folder"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
