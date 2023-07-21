#!/usr/bin/python3
<<<<<<< HEAD
""" A Fabric script That Deploys archive!
"""
from fabric.api import env, put, run
from os.path import exists
env.hosts = ['100.25.102.18', '54.237.30.210']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes a .tgz archive from the contents of `web_static/` in AirBnB
    clone repo to the web servers
    Retuns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if not exists(archive_path) or archive_path is None:

        return False

    file_name = archive_path.split('/')[-1]
    dir_name = file_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(dir_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        file_name, dir_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(dir_name) +
        '/data/web_static/releases/{}/'.format(dir_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(dir_name))
    run('rm -rf /data/web_static/

current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        dir_name))

    print('New version deployed!')
    return True
=======
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["34.201.165.189", "54.236.30.97"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
>>>>>>> b7bd53f53b3d33e16d6c38c4ef24682b48d1f8c9
