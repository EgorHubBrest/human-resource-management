"""
Module for installing app.
"""
from setuptools import setup, find_packages


def require_pakages():
    """
    Function for parsing file requirements.txt return: list of packages for install_requires.
    """

    with open("requirements.txt") as file_requirements:
        packages = [lib.replace('\n', '') for lib in file_requirements.readlines()]
        return packages


setup(name="department-app",
	version="0.1",
	description="Django app for human resourse management.",
	lond_description=open("README.md").read(),
	packages=find_packages(),
	url="https://github.com/krisstinkou/human-resource-management.git",
	install_requires=require_pakages()
)
