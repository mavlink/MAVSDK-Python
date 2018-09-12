# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path, getcwd


def parse_requirements(filename):
    """
    Helper which parses requirement_?.*.txt files

    :param filename: relative path, e.g. `./requirements.txt`
    :returns: List of requirements
    """

    # Get absolute filepath
    filepath = path.join(getcwd(), filename)

    # Check if file exists
    if not path.exists(filepath):
        print("[!] File {} not found".format(filename))
        return []

    # Parse install requirements
    with open(filepath, encoding="utf-8") as f:
        return [requires.strip() for requires in f.readlines()]


def parse_long_description():
    """
    Helper function which parses the readme

    :returns: Content of the Readme
    """
    with open(path.join(getcwd(), "README.rst"), encoding="utf-8") as f:
        return f.read()


setup(
    name="dronecode-sdk",
    version="0.1.0a",
    description="Pythonwrapper for Dronecode SDK",
    long_description=parse_long_description(),
    url="https://github.com/dronecode/DronecodeSDK-Python",
    author="@TODO",
    author_email="@TODO",

    classifiers=[
        "Development Status :: 3 - Production/Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],

    packages=find_packages(exclude=["other", "docs", "tests", "examples",
                                    "proto"]),
    install_requires=parse_requirements("requirements.txt"),
    setup_requires=parse_requirements("requirements-dev.txt"),

    project_urls={
        "Bug Reports": "https://github.com/dronecode/DronecodeSDK-Python/issues",
        "Source": "https://github.com/dronecode/DronecodeSDK-Python/",
    },

)
