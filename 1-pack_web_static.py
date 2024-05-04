#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(date)
    archive_path = "versions/{}".format(archive_name)

    if not os.path.exists("versions"):
        os.mkdir("versions")

    print("Packing web_static to {}".format(archive_path))
    command = "tar -cvzf {} web_static".format(archive_path)
    result = local(command)

    if result.failed:
        return None
    else:
        print("web_static packed: {} -> {}Bytes".format(archive_path, os.path.getsize(archive_path)))
        return archive_path

