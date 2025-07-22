# -*- coding: utf-8 -*-
from distutils.command.build import build
from setuptools import setup, find_packages
from codecs import open
from os import path, getcwd

import urllib.request
import os
import stat
import platform
import subprocess


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
        Trying to detect the platform to know which `mavsdk_server` executable
        to download
        """
        if platform.system() == 'Linux' and 'MAVSDK_SERVER_ARCH' in os.environ:
            if os.environ['MAVSDK_SERVER_ARCH'] == "armv6l":
                return 'linux-armv6-musl'
            elif os.environ['MAVSDK_SERVER_ARCH'] == "armv7l":
                return 'linux-armv7l-musl'
            elif os.environ['MAVSDK_SERVER_ARCH'] == "aarch64":
                return 'linux-arm64-musl'
            else:
                raise NotImplementedError(
                    "Error: unknown MAVSDK_SERVER_ARCH: "
                    f"{os.environ['MAVSDK_SERVER_ARCH']}")
        elif platform.system() == 'Linux':
            return 'musl_x86_64'
        elif platform.system() == 'Darwin':
            if platform.processor() == 'i386':
                return 'macos_x64'
            elif platform.processor() == 'arm':
                return 'macos_arm64'
            raise NotImplementedError(
                f"Error: unknown macOS processor: {platform.processor()}")
        elif platform.system() == 'Windows' \
                and (platform.processor().startswith('AMD64') or
                     platform.processor().startswith('Intel64')):
            return 'win_x64.exe'
        else:
            raise NotImplementedError(
                "Error: mavsdk_server is not distributed for platform "
                f"{platform.system()} ({platform.processor()}) (yet)!\n\n"
                "You should set the 'MAVSDK_BUILD_PURE=ON' environment "
                "variable and get mavsdk_server manually.")

    @property
    def mavsdk_server_filepath(self):
        """
        The location of the downloaded `mavsdk_server` binary
        For Windows this needs to be a .exe file
        """
        if platform.system() == 'Windows':
            return 'mavsdk/bin/mavsdk_server.exe'
        else:
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
        return "https://github.com/mavlink/MAVSDK/releases/download/" \
            f"{self.mavsdk_server_tag}/mavsdk_server_{self.platform_suffix}"

    def run(self):
        if 'MAVSDK_BUILD_PURE' not in os.environ:
            self.download_mavsdk_server()

        build.run(self)

    def download_mavsdk_server(self):
        print(
            f"downloading {self.mavsdk_server_url} into "
            f"{self.mavsdk_server_filepath}")
        urllib.request.urlretrieve(
            self.mavsdk_server_url,
            filename=self.mavsdk_server_filepath)

        print(f"adding execution permission to {self.mavsdk_server_filepath}")
        st = os.stat(self.mavsdk_server_filepath)
        os.chmod(self.mavsdk_server_filepath, st.st_mode | stat.S_IEXEC)


def version():
    process = subprocess.Popen(["git", "describe", "--tags"],
                               stdout=subprocess.PIPE)
    output, _ = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        raise RuntimeError(f"git describe command exited with: {exit_code}")
    git_describe_str = output.decode("utf-8").strip()
    git_describe_str = git_describe_str.replace("-g", "+g")
    print(git_describe_str)
    return git_describe_str


setup(
    name="mavsdk",
    version=version(),
    description="Python wrapper for MAVSDK",
    long_description=parse_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/mavlink/MAVSDK-Python",
    maintainer="Jonas Vautherin, Julian Oes",
    maintainer_email="jonas@auterion.com, julian.oes@auterion.com",
    python_requires='>=3.7',
    include_package_data=True,
    cmdclass={'build': custom_build},

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
    ],

    packages=find_packages(exclude=["other", "docs", "tests", "examples",
                                    "proto"]),
    install_requires=parse_requirements("requirements.txt"),

    project_urls={
        "Bug Reports": "https://github.com/mavlink/MAVSDK-Python/issues",
        "Source": "https://github.com/mavlink/MAVSDK-Python/",
    },
)
