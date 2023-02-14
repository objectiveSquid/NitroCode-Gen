from pkg_resources import DistributionNotFound, VersionConflict, require
from os import name, system
from sys import argv


def install_requirements(needed_requirements: list):
    if name == "nt":
        for requirement in needed_requirements:
            system(f"py -m pip install {requirement}")
    else:
        for requirement in needed_requirements:
            system(f"python3 -m pip install {requirement}")


def check_requirements():
    with open("requirements.txt", "r") as requirements_file:
        requirements = requirements_file.readlines()
    needed_requirements = []
    for requirement in requirements:
        try:
            require(requirement)
        except DistributionNotFound or VersionConflict:
            needed_requirements.append(requirement)
    return needed_requirements
