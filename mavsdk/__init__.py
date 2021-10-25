# -*- coding: utf-8 -*-

import asyncio
import platform
import sys

from .system import System

# Check for compatibility
(major, minor, _) = platform.python_version_tuple()
if not ((int(major) >= 3 and int(minor) >= 6) or (int(major) >= 4)):
    print("[!] MAVSDK-Python is only available on Python >= 3.6")
    sys.exit(1)

# Do asyncio specific initialization
try:
    # Try to import uvloop, provides _MUCH_ better performance compared to the
    # standart unix selector event loop
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    # No uvloop installed on the system; the default eventloop works as well!
    pass
