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


# This project is published under two names during the transition to MAVSDK v4:
#
#   - "mavsdk-grpc" is the going-forward name of this gRPC-based wrapper.
#   - "mavsdk" is the legacy name. It is being handed over to the new native
#     binding that lives in the main MAVSDK repository, and is published from
#     here one last time (carrying a warning) so that users get a heads-up
#     before `pip install mavsdk` starts resolving to a different API.
#
# The legacy name is the one that needs opting into, so that a plain build
# produces the going-forward package.
LEGACY_DIST_NAME = "mavsdk"
DEFAULT_DIST_NAME = "mavsdk-grpc"

DIST_NAME = os.environ.get("MAVSDK_DIST_NAME", DEFAULT_DIST_NAME)

if DIST_NAME not in (DEFAULT_DIST_NAME, LEGACY_DIST_NAME):
    raise RuntimeError(
        f"Unknown MAVSDK_DIST_NAME: '{DIST_NAME}'. "
        f"Expected '{DEFAULT_DIST_NAME}' or '{LEGACY_DIST_NAME}'."
    )

# The two distributions must install under *different* import names, otherwise
# they silently overwrite each other's files when both end up in the same
# environment (which is easy to hit through transitive dependencies, since pip
# has no way to express a conflict between them).
#
# Everything inside the package imports relatively, so remapping the install
# name here is enough -- no source file needs to know about it.
SOURCE_PACKAGE = "mavsdk"
IMPORT_NAME = "mavsdk" if DIST_NAME == LEGACY_DIST_NAME else "mavsdk_grpc"


def remapped_packages():
    """
    Find the packages under `mavsdk/` and re-root them at IMPORT_NAME.

    :returns: list of package names as they will be installed
    """
    found = find_packages(exclude=["other", "docs", "tests", "examples", "proto"])
    return [
        IMPORT_NAME + pkg[len(SOURCE_PACKAGE) :]
        for pkg in found
        if pkg == SOURCE_PACKAGE or pkg.startswith(SOURCE_PACKAGE + ".")
    ]


MIGRATION_URL = "https://mavsdk.mavlink.io/main/en/python/migration.html"

LEGACY_NOTICE = f"""\
> ## ⚠️ This package has been renamed to `mavsdk-grpc`
>
> This is the last release of the gRPC wrapper under the `mavsdk` name. That
> name on PyPI now belongs to the native MAVSDK binding, which has a
> **different API** and does not depend on gRPC.
>
> * **To carry on with this API**, install
>   [`mavsdk-grpc`](https://pypi.org/project/mavsdk-grpc/) and import it as
>   `mavsdk_grpc`. The code is identical, so `import mavsdk_grpc as mavsdk` is
>   enough if you would rather not touch anything else. Development continues
>   there, including releases tracking MAVSDK v4. It deliberately installs under
>   a separate import name, so it can never collide with the native binding.
> * **To freeze**, pin `mavsdk<4`. This release keeps working, but will not
>   receive any further updates.
> * **To move to the native binding**, see <{MIGRATION_URL}>.

"""


def dist_metadata():
    """
    Build the name/description/long_description trio for the distribution being
    built, so that the legacy name carries the rename notice on its PyPI page.

    :returns: dict of keyword arguments for setup()
    """
    long_description = parse_long_description()

    if DIST_NAME == LEGACY_DIST_NAME:
        return {
            "name": LEGACY_DIST_NAME,
            "description": (
                "Deprecated, renamed to 'mavsdk-grpc' "
                "(the 'mavsdk' name now refers to the native MAVSDK binding)"
            ),
            "long_description": LEGACY_NOTICE + long_description,
        }

    return {
        "name": DEFAULT_DIST_NAME,
        "description": "gRPC-based Python wrapper for MAVSDK",
        "long_description": long_description,
    }


def write_dist_marker():
    """
    Record which distribution this build belongs to, so that `mavsdk/__init__.py`
    can decide at runtime whether to warn about the rename. The sources are
    shared between the two distributions, so there is nothing else to tell them
    apart from the inside.

    The generated file is not committed; see .gitignore.
    """
    marker_path = path.join(path.dirname(path.abspath(__file__)), "mavsdk", "_dist.py")
    with open(marker_path, "w", encoding="utf-8") as f:
        f.write(
            "# Generated by setup.py at build time. Do not edit or commit.\n"
            f'DIST_NAME = "{DIST_NAME}"\n'
        )


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
        if platform.system() == "Linux" and "MAVSDK_SERVER_ARCH" in os.environ:
            if os.environ["MAVSDK_SERVER_ARCH"] == "armv6l":
                return "linux-armv6-musl"
            elif os.environ["MAVSDK_SERVER_ARCH"] == "armv7l":
                return "linux-armv7l-musl"
            elif os.environ["MAVSDK_SERVER_ARCH"] == "aarch64":
                return "linux-arm64-musl"
            else:
                raise NotImplementedError(
                    "Error: unknown MAVSDK_SERVER_ARCH: "
                    f"{os.environ['MAVSDK_SERVER_ARCH']}"
                )

        elif platform.system() == "Linux":
            return "musl_x86_64"

        elif platform.system() == "Darwin":
            if platform.processor() == "i386":
                return "macos_x64"
            elif platform.processor() == "arm":
                return "macos_arm64"
            raise NotImplementedError(
                f"Error: unknown macOS processor: {platform.processor()}"
            )

        elif platform.system() == "Windows" and "MAVSDK_SERVER_ARCH" in os.environ:
            # The released Windows assets are named with a .exe suffix, e.g.
            # mavsdk_server_win_x86.exe -- without it the download 404s.
            if os.environ["MAVSDK_SERVER_ARCH"] == "x86":
                return "win_x86.exe"
            elif os.environ["MAVSDK_SERVER_ARCH"] == "x64":
                return "win_x64.exe"
            elif os.environ["MAVSDK_SERVER_ARCH"] == "arm64":
                return "win_arm64.exe"
            else:
                raise NotImplementedError(
                    "Error: unknown MAVSDK_SERVER_ARCH: "
                    f"{os.environ['MAVSDK_SERVER_ARCH']}"
                )

        elif platform.system() == "Windows" and (
            platform.processor().startswith("AMD64")
            or platform.processor().startswith("Intel64")
        ):
            # Fallback
            return "win_x64.exe"
        else:
            raise NotImplementedError(
                "Error: mavsdk_server is not distributed for platform "
                f"{platform.system()} ({platform.processor()}) (yet)!\n\n"
                "You should set the 'MAVSDK_BUILD_PURE=ON' environment "
                "variable and get mavsdk_server manually."
            )

    @property
    def mavsdk_server_filepath(self):
        """
        The location of the downloaded `mavsdk_server` binary
        For Windows this needs to be a .exe file
        """
        if platform.system() == "Windows":
            return "mavsdk/bin/mavsdk_server.exe"
        else:
            return "mavsdk/bin/mavsdk_server"

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
        return (
            "https://github.com/mavlink/MAVSDK/releases/download/"
            f"{self.mavsdk_server_tag}/mavsdk_server_{self.platform_suffix}"
        )

    def run(self):
        if "MAVSDK_BUILD_PURE" not in os.environ:
            self.download_mavsdk_server()

        build.run(self)

    def download_mavsdk_server(self):
        print(
            f"downloading {self.mavsdk_server_url} into {self.mavsdk_server_filepath}"
        )
        urllib.request.urlretrieve(
            self.mavsdk_server_url, filename=self.mavsdk_server_filepath
        )

        print(f"adding execution permission to {self.mavsdk_server_filepath}")
        st = os.stat(self.mavsdk_server_filepath)
        os.chmod(self.mavsdk_server_filepath, st.st_mode | stat.S_IEXEC)


def version():
    process = subprocess.Popen(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        raise RuntimeError(f"git describe command exited with: {exit_code}")
    git_describe_str = output.decode("utf-8").strip()
    git_describe_str = git_describe_str.replace("-g", "+g")
    print(git_describe_str)
    return git_describe_str


write_dist_marker()

setup(
    version=version(),
    long_description_content_type="text/markdown",
    **dist_metadata(),
    url="https://github.com/mavlink/MAVSDK-Python",
    maintainer="Jonas Vautherin, Julian Oes",
    maintainer_email="dev@jonas.vautherin.ch, julian@oes.ch",
    python_requires=">=3.7",
    include_package_data=True,
    cmdclass={"build": custom_build},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=remapped_packages(),
    package_dir={IMPORT_NAME: SOURCE_PACKAGE},
    install_requires=parse_requirements("requirements.txt"),
    project_urls={
        "Bug Reports": "https://github.com/mavlink/MAVSDK-Python/issues",
        "Source": "https://github.com/mavlink/MAVSDK-Python/",
    },
)
