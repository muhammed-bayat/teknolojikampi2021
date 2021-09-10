import os 
import apt
import sys


def installedPackages():
    os.system('sudo apt list --installed')
    x = os.system('echo $?')
    if x>0:
        print('installed')
    else:
        print('not installed')

installedPackages()

