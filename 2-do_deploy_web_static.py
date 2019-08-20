#!/usr/bin/python3
# Distributes an archive to web servers

from fabric.api import env, put, run
import os

env.hosts = ["35.237.201.27", "35.243.139.79"]


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    
    if not os.path.exists(archive_path):
        return False
    file_long = archive_path.split("/")[-1]
    fname = file_long.split(".")[0]
    x = put(archive_path, "/tmp/{}.tgz".format(fname))
    if x.failed:
        return False
    x = run("mkdir -p /data/web_static/releases/{}/".format(fname))
    if x.failed:
        return False
    x = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(fname, fname))
    if x.failed:
        return False
    x = run("rm /tmp/{}.tgz".format(fname))
    if x.failed:
        return False
    x = run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(fname, fname))
    if x.failed:
        return False
    x = run("rm -rf /data/web_static/releases/{}/web_static".
            format(fname))
    if x.failed:
        return False
    x = run("rm -rf /data/web_static/current")
    if x.failed:
        return False
    x = run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(fname))
    if x.failed:
        return False
    print("New version deployed!")
    return True
