#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.tune import (SongElement, TuneDescription, TuneError)


async def run():

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    song_elements = []
    song_elements.append(SongElement.DURATION_4)
    song_elements.append(SongElement.NOTE_G)
    song_elements.append(SongElement.NOTE_A)
    song_elements.append(SongElement.NOTE_B)
    song_elements.append(SongElement.FLAT)
    song_elements.append(SongElement.OCTAVE_UP)
    song_elements.append(SongElement.DURATION_1)
    song_elements.append(SongElement.NOTE_E)
    song_elements.append(SongElement.FLAT)
    song_elements.append(SongElement.OCTAVE_DOWN)
    song_elements.append(SongElement.DURATION_4)
    song_elements.append(SongElement.NOTE_PAUSE)
    song_elements.append(SongElement.NOTE_F)
    song_elements.append(SongElement.NOTE_G)
    song_elements.append(SongElement.NOTE_A)
    song_elements.append(SongElement.OCTAVE_UP)
    song_elements.append(SongElement.DURATION_2)
    song_elements.append(SongElement.NOTE_D)
    song_elements.append(SongElement.NOTE_D)
    song_elements.append(SongElement.OCTAVE_DOWN)
    song_elements.append(SongElement.DURATION_4)
    song_elements.append(SongElement.NOTE_PAUSE)
    song_elements.append(SongElement.NOTE_E)
    song_elements.append(SongElement.FLAT)
    song_elements.append(SongElement.NOTE_F)
    song_elements.append(SongElement.NOTE_G)
    song_elements.append(SongElement.OCTAVE_UP)
    song_elements.append(SongElement.DURATION_1)
    song_elements.append(SongElement.NOTE_C)
    song_elements.append(SongElement.OCTAVE_DOWN)
    song_elements.append(SongElement.DURATION_4)
    song_elements.append(SongElement.NOTE_PAUSE)
    song_elements.append(SongElement.NOTE_A)
    song_elements.append(SongElement.OCTAVE_UP)
    song_elements.append(SongElement.NOTE_C)
    song_elements.append(SongElement.OCTAVE_DOWN)
    song_elements.append(SongElement.NOTE_B)
    song_elements.append(SongElement.FLAT)
    song_elements.append(SongElement.DURATION_2)
    song_elements.append(SongElement.NOTE_G)

    tune_description = TuneDescription(song_elements, 200)
    await drone.tune.play_tune(tune_description)

    print("Tune played")

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
