# -*- coding: utf-8 -*-

import asyncio
import platform
import sys
import warnings

from .system import System

# Check for compatibility
(major, minor, _) = platform.python_version_tuple()
if not ((int(major) >= 3 and int(minor) >= 6) or (int(major) >= 4)):
    print("[!] MAVSDK-Python is only available on Python >= 3.6")
    sys.exit(1)

# Written by setup.py at build time. Absent when running from a source checkout,
# in which case there is nothing to warn about.
try:
    from ._dist import DIST_NAME as _dist_name
except ImportError:
    _dist_name = None

if _dist_name == "mavsdk":
    # A FutureWarning rather than a DeprecationWarning: the latter is filtered
    # out by default unless it is raised from __main__, which would hide this
    # from exactly the people who need to see it.
    warnings.warn(
        "The 'mavsdk' package has been renamed to 'mavsdk-grpc'. This is the "
        "last release of the gRPC wrapper under the 'mavsdk' name: that name "
        "now refers to the native MAVSDK binding, which has a different API.\n"
        "  To carry on with this API, install 'mavsdk-grpc' and use "
        "'import mavsdk_grpc as mavsdk'. The code is identical, development "
        "continues there (including releases for MAVSDK v4), and it installs "
        "under a separate import name so it cannot collide with the native "
        "binding.\n"
        "  To freeze instead, pin 'mavsdk<4' (no further updates).\n"
        "  To migrate, see https://mavsdk.mavlink.io/main/en/python/",
        FutureWarning,
        stacklevel=2,
    )

# Do asyncio specific initialization
try:
    # Try to import uvloop, provides _MUCH_ better performance compared to the
    # standard unix selector event loop
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    # No uvloop installed on the system; the default eventloop works as well!
    pass
