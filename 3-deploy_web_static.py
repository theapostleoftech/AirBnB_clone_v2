#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""
from fabric.api import env, local, run, put
from datetime import datetime
from os.path import exists

# Define your server IPs and user
env.hosts = ['52.86.208.90', '54.166.135.118']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'  # Define your SSH private key here


def do_pack():
    """
    Creates a compressed archive of the web_static folder
    """
    try:
        local("mkdir -p versions")
        time_format = "%Y%m%d%H%M%S"
        archive_name = "versions/web_static_{}.tgz".format(
            datetime.now().strftime(time_format))
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploys the archive to the web servers.
    """
    if not exists(archive_path):
        print("Archive not found: {}".format(archive_path))
        return False

    # Extract file name and directory paths from archive_path
    file_name = archive_path.split("/")[-1]
    no_ext = file_name.replace('.tgz', '')
    dest_path = "/data/web_static/releases/" + no_ext + "/"

    try:
        # Upload archive to the /tmp/ directory
        put(archive_path, "/tmp/" + file_name)

        # Create directory where we will uncompress
        run("mkdir -p {}".format(dest_path))

        # Uncompress the archive to the folder on the server
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_path))

        # Delete the archive from the server
        run("rm /tmp/{}".format(file_name))

        # Move contents out of the 'web_static' folder from the tar archive
        run("mv {0}/web_static/* {0}/".format(dest_path))

        # Remove the empty directory
        run("rm -rf {}/web_static".format(dest_path))

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(dest_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False


def deploy():
    """
    Deploys the latest version of the web_static folder to the web servers
    """
    archive_path = do_pack()
    if not archive_path:
        print("Failed to create archive.")
        return False
    return do_deploy(archive_path)
