#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Provide the mavsdk_server binary for the current platform.

This is the hatch-friendly equivalent of the custom build step in setup.py
(see ``custom_build`` there).

If a local MAVSDK C++ build is available it is preferred: this lets you run
against a ``mavsdk_server`` built from a patched ``MAVSDK`` checkout instead
of the stock release binary. The C++ project root is taken from the
``MAVSDK_CPP_PROJECT_ROOT`` environment variable and defaults to
``../trusk-mavsdk-cpp``. The newest ``mavsdk_server`` binary found below that
root is copied into ``mavsdk/bin/``.

Otherwise, the release tag is read from ``MAVSDK_SERVER_VERSION`` and the
matching ``mavsdk_server`` binary is downloaded from GitHub into ``mavsdk/bin/``.

When building on Linux for an ARM board (e.g. a Raspberry Pi), set
``MAVSDK_SERVER_ARCH`` to one of ``armv6l``, ``armv7l`` or ``aarch64``. It
defaults to ``aarch64`` when not set.

Set ``MAVSDK_BUILD_PURE`` to skip the download entirely.
"""

import os
import platform
import shutil
import stat
import sys
import urllib.request


def get_platform_suffix():
    """Return the ``mavsdk_server`` asset suffix for the current platform."""
    if platform.system() == "Linux" and "MAVSDK_SERVER_ARCH" in os.environ:
        arch = os.environ["MAVSDK_SERVER_ARCH"]
        if arch in ("armv6l", "armv6"):
            return "linux-armv6-musl"
        elif arch in ("armv7l", "armv7"):
            return "linux-armv7l-musl"
        elif arch == "aarch64":
            return "linux-arm64-musl"
        elif arch in ("x86_64", "amd64"):
            return "musl_x86_64"
        raise NotImplementedError(f"Error: unknown MAVSDK_SERVER_ARCH: {arch}")

    elif platform.system() == "Linux":
        return "musl_x86_64"

    elif platform.system() == "Darwin":
        if platform.processor() == "i386":
            return "macos_x64"
        elif platform.processor() == "arm":
            return "macos_arm64"
        raise NotImplementedError(f"Error: unknown macOS processor: {platform.processor()}")

    elif platform.system() == "Windows" and "MAVSDK_SERVER_ARCH" in os.environ:
        # The released Windows assets are named with a .exe suffix, e.g.
        # mavsdk_server_win_x86.exe -- without it the download 404s.
        arch = os.environ["MAVSDK_SERVER_ARCH"]
        if arch == "x86":
            return "win_x86.exe"
        elif arch == "x64":
            return "win_x64.exe"
        elif arch == "arm64":
            return "win_arm64.exe"
        raise NotImplementedError(f"Error: unknown MAVSDK_SERVER_ARCH: {arch}")

    elif platform.system() == "Windows" and (
        platform.processor().startswith("AMD64") or platform.processor().startswith("Intel64")
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


def get_cpp_project_root():
    """Return the absolute path of the local MAVSDK C++ project.

    Uses the ``MAVSDK_CPP_PROJECT_ROOT`` environment variable, defaulting to
    ``../trusk-mavsdk-cpp`` relative to the current working directory.
    """
    root = os.environ.get("MAVSDK_CPP_PROJECT_ROOT", os.path.join("..", "trusk-mavsdk-cpp"))
    return os.path.abspath(root)


def find_local_server(cpp_project_root):
    """Find the newest ``mavsdk_server`` binary below ``cpp_project_root``.

    Returns the absolute path of the newest executable, or ``None`` if no
    candidate is found (or the root does not exist). Heavy directories that
    never contain the binary (``.git``, ``third_party``) are pruned so the
    walk stays fast even on a fully populated build tree.
    """
    if not os.path.isdir(cpp_project_root):
        return None

    is_windows = platform.system() == "Windows"
    binary_name = "mavsdk_server.exe" if is_windows else "mavsdk_server"

    candidates = []
    for dirpath, dirnames, filenames in os.walk(cpp_project_root):
        # Prune directories that cannot contain the server binary.
        dirnames[:] = [d for d in dirnames if d not in (".git", "third_party")]

        if binary_name not in filenames:
            continue

        candidate = os.path.join(dirpath, binary_name)
        # On non-Windows the binary must be executable; on Windows the file
        # attribute is not a reliable signal, so accept any match.
        if not is_windows and not os.access(candidate, os.X_OK):
            continue

        try:
            mtime = os.stat(candidate).st_mtime
        except OSError:
            continue
        candidates.append((mtime, candidate))

    if not candidates:
        return None

    candidates.sort(reverse=True)
    return candidates[0][1]


def copy_local_server(src, dst):
    """Copy ``src`` to ``dst``, adding the execution permission."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    st = os.stat(dst)
    os.chmod(dst, st.st_mode | stat.S_IEXEC)


def main():
    # ARM Linux builds need to pick a server architecture; default to aarch64
    # (e.g. a Raspberry Pi running a 64-bit distribution).
    if "MAVSDK_SERVER_ARCH" not in os.environ and platform.system() == "Linux":
        os.environ["MAVSDK_SERVER_ARCH"] = "aarch64"

    if "MAVSDK_BUILD_PURE" in os.environ:
        print("[!] MAVSDK_BUILD_PURE is set, skipping mavsdk_server download")
        return

    if platform.system() == "Windows":
        filepath = "mavsdk/bin/mavsdk_server.exe"
    else:
        filepath = "mavsdk/bin/mavsdk_server"

    # Prefer a locally built server so that patched MAVSDK C++ sources are
    # used. Fall back to downloading the release binary otherwise.
    cpp_project_root = get_cpp_project_root()
    local_server = find_local_server(cpp_project_root)
    if local_server is not None:
        print(f"Found local mavsdk_server: {local_server}")
        print(f"Copying it into {filepath}")
        copy_local_server(local_server, filepath)
        print(
            "[!] The copied binary links against shared libraries in the C++ build "
            f"directory (RUNPATH points into {cpp_project_root}). Keep the build "
            "directory around, or set LD_LIBRARY_PATH accordingly, when using it."
        )
        return

    if os.path.isdir(cpp_project_root):
        print(
            f"[!] No mavsdk_server binary found under {cpp_project_root}, "
            "falling back to the release download.",
            file=sys.stderr,
        )
    else:
        print(
            f"[!] {cpp_project_root} does not exist, falling back to the "
            "release download.",
            file=sys.stderr,
        )

    with open("MAVSDK_SERVER_VERSION") as mavsdk_server_version_file:
        tag = mavsdk_server_version_file.read().rstrip()

    url = (
        "https://github.com/mavlink/MAVSDK/releases/download/"
        f"{tag}/mavsdk_server_{get_platform_suffix()}"
    )

    os.makedirs("mavsdk/bin", exist_ok=True)
    print(f"Downloading {url} into {filepath}")
    urllib.request.urlretrieve(url, filename=filepath)

    print(f"Adding execution permission to {filepath}")
    st = os.stat(filepath)
    os.chmod(filepath, st.st_mode | stat.S_IEXEC)


if __name__ == "__main__":
    main()
