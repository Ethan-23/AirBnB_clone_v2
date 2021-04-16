#!/usr/bin/python3
"""Comment"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Fabric .tgz archive"""

    name = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(name))
    except:
        return None
    return "versions/web_static_{}.tgz web_static".format(name)
