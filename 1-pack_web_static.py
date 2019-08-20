#!/usr/bin/python3
# Generates a .tgz archive from the contents of a folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs files from specified directory into .tgz file"""
    dt = datetime.now()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    local('mkdir -p versions')
    x = local("tar -cvzf " + file + " ./web_static/")
    if x.succeeded:
        return file
    return None
