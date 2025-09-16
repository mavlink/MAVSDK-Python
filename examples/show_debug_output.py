#!/usr/bin/env python3
"""
Test to see all output including debug messages
"""

import asyncio
import logging
from mavsdk import System

# Setup logging to see EVERYTHING
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


async def test_see_all():
    print("Testing with DEBUG level to see all messages...")

    drone = System()
    try:
        await asyncio.wait_for(drone.connect("invalid://bad:connection"), timeout=8)
    except asyncio.TimeoutError:
        print("Timed out - all messages should be visible above")
    except Exception as e:
        print(f"Got exception: {e}")


if __name__ == "__main__":
    asyncio.run(test_see_all())
