# -*- coding: utf-8 -*-
from distutils.command.build import build
from setuptools import setup, find_packages
from codecs import open
from os import path, getcwd

import urllib.request
import os
import stat
import sys


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
    with open(path.join(getcwd(), "README.md"), encoding="utf-8") as f:
        return f.read()


class custom_build(build):
    """
    Class that overrides the build step to add a custom pre-build step
    """

    @property
    def platform_suffix(self):
        """
        Trying to detect the platform to know which `mavsdk_server` executable to download
        """
        if sys.platform.startswith('linux'):
            return 'manylinux1-x64'
        else:
            raise NotImplementedError(
                f"Platform {sys.platform} is not (yet) supported by this setup.py!")

    @property
    def mavsdk_server_filepath(self):
        """
        The location of the downloaded `mavsdk_server` binary
        """
        return 'mavsdk/bin/mavsdk_server'

    @property
    def mavsdk_server_tag(self):
        """
        The release tag of the `mavsdk_server` binary is defined in the file 
        "MAVSDK_SERVER_VERSION", and used to download the corresponding release
        """
        with open("MAVSDK_SERVER_VERSION") as mavsdk_server_version_file:
            return mavsdk_server_version_file.read().rstrip()

    @property
    def mavsdk_server_url(self):
        """
        Build the url of the `mavsdk_server` binary
        """
        return f"https://github.com/mavlink/MAVSDK/releases/download/{self.mavsdk_server_tag}/mavsdk_server_{self.platform_suffix}"

    def run(self):
        self.download_mavsdk_server()
        build.run(self)

    def download_mavsdk_server(self):
        print(
            f"downloading {self.mavsdk_server_url} into {self.mavsdk_server_filepath}")
        urllib.request.urlretrieve(
            self.mavsdk_server_url,
            filename=self.mavsdk_server_filepath)

        print(f"adding execution permission to {self.mavsdk_server_filepath}")
        st = os.stat(self.mavsdk_server_filepath)
        os.chmod(self.mavsdk_server_filepath, st.st_mode | stat.S_IEXEC)


setup(
    name="mavsdk",
    version="0.2.0",
    description="Python wrapper for MAVSDK",
    long_description=parse_long_description(),
    url="https://github.com/mavlink/MAVSDK-Python",
    maintainer="Jonas Vautherin, Julian Oes",
    maintainer_email="jonas@auterion.com, julian.oes@auterion.com",
    python_requires='>=3.6',
    include_package_data=True,
    cmdclass={'build': custom_build},

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],

    packages=find_packages(exclude=["other", "docs", "tests", "examples",
                                    "proto"]),
    install_requires=parse_requirements("requirements.txt"),
    setup_requires=parse_requirements("requirements-dev.txt"),

    project_urls={
        "Bug Reports": "https://github.com/mavlink/MAVSDK-Python/issues",
        "Source": "https://github.com/mavlink/MAVSDK-Python/",
    },
)
