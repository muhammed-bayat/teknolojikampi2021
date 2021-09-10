import os 
import apt
import sys



def sorgulaOs():
    pkg_name="python"
    os.system('sudo apt list --installed | {pkg_name}'.format(pkg_name=pkg_name))
    x = os.system('echo $?')
    if x>0:
        print('installed')
    else:
        print('not installed')

sorgulaOs()