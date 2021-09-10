import os 
import apt
import sys


def getir():
	cache = apt.Cache()
	print(list(pkg.name for pkg in cache if pkg.is_installed))

getir()
"""
def parametreligetir(parametre):
    cache = apt.Cache()
	print(parametre in (pkg.name for pkg in cache if pkg.is_installed))

parametreligetir("python")"""