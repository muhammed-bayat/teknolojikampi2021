import os 
import apt
import sys


def sorgulaPkg():
    pkg_name = "python"
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    pkg = cache[pkg_name]
    if pkg.is_installed:
        print ("{pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        print('not installed')

sorgulaPkg()
