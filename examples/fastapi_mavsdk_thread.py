#!/usr/bin/env python3

"""
Control a drone from a web API (FastAPI) by running MAVSDK in its own thread.

Why: MAVSDK-Python uses gRPC's asyncio API, and the gRPC channel is bound to
the event loop that was running when `System.connect()` was called. Awaiting a
MAVSDK call from any other event loop (e.g. uvicorn's loop when the web server
runs in a separate thread, or a second `asyncio.run()`) fails with:

    RuntimeError: Task <...> got Future <...> attached to a different loop

The pattern below gives MAVSDK one dedicated event loop in a background
thread. Everything else (web handlers, a video/OpenCV loop, a GUI, plain
threads) hands coroutines over to that loop with
`asyncio.run_coroutine_threadsafe()` instead of awaiting MAVSDK directly. The
other loops are never blocked by MAVSDK and MAVSDK is never touched from the
wrong loop.

Requires: pip install fastapi uvicorn

Run:
    python3 fastapi_mavsdk_thread.py
    curl localhost:8000/telemetry
    curl -X POST localhost:8000/arm
    curl -X POST localhost:8000/takeoff
    curl -X POST localhost:8000/land
"""

import asyncio
import threading
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException

from mavsdk_grpc import System
from mavsdk_grpc.action import ActionError


class MavsdkThread:
    """Owns a System and the one event loop it is allowed to run on."""

    def __init__(self, system_address="udpin://0.0.0.0:14540"):
        self._system_address = system_address
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._loop.run_forever, name="mavsdk", daemon=True)
        self._telemetry_task = None
        self.drone = System()
        # Latest telemetry. Written on the MAVSDK loop only, read from anywhere.
        self.position = None
        self.is_armed = None

    def submit(self, coro):
        """Schedule `coro` on the MAVSDK loop, from any thread.

        Returns a concurrent.futures.Future.
        """
        return asyncio.run_coroutine_threadsafe(coro, self._loop)

    def run(self, coro, timeout=None):
        """Run `coro` on the MAVSDK loop and block until it returns.

        For use from plain (non-async) threads, e.g. a video loop.
        """
        return self.submit(coro).result(timeout)

    async def run_async(self, coro):
        """Await `coro` from *another* event loop (e.g. a FastAPI handler)."""
        return await asyncio.wrap_future(self.submit(coro))

    def start(self, timeout=30):
        self._thread.start()
        self.run(self._connect(), timeout)

    def stop(self):
        if self._telemetry_task is not None:
            self._loop.call_soon_threadsafe(self._telemetry_task.cancel)
        self._loop.call_soon_threadsafe(self._loop.stop)
        self._thread.join(timeout=5)

    async def _connect(self):
        # connect() must run on the MAVSDK loop: this is what binds the
        # gRPC channel to it.
        await self.drone.connect(system_address=self._system_address)
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                break
        # Long-running subscriptions live on the MAVSDK loop too. Keep a
        # reference to the task so it is not garbage collected.
        self._telemetry_task = asyncio.ensure_future(self._watch_telemetry())

    async def _watch_telemetry(self):
        async def position():
            async for p in self.drone.telemetry.position():
                self.position = p

        async def armed():
            async for a in self.drone.telemetry.armed():
                self.is_armed = a

        await asyncio.gather(position(), armed())


mavsdk_thread = MavsdkThread()


@asynccontextmanager
async def lifespan(app):
    # start() blocks until connected; keep it off the web server's loop.
    await asyncio.to_thread(mavsdk_thread.start)
    yield
    mavsdk_thread.stop()


app = FastAPI(lifespan=lifespan)


async def _action(coro):
    try:
        await mavsdk_thread.run_async(coro)
    except ActionError as error:
        raise HTTPException(status_code=409, detail=str(error)) from error
    return {"result": "ok"}


@app.get("/telemetry")
async def telemetry():
    p = mavsdk_thread.position
    return {
        "armed": mavsdk_thread.is_armed,
        "position": None
        if p is None
        else {
            "latitude_deg": p.latitude_deg,
            "longitude_deg": p.longitude_deg,
            "relative_altitude_m": p.relative_altitude_m,
        },
    }


@app.post("/arm")
async def arm():
    # Note: the coroutine object is created here but only *runs* on the
    # MAVSDK loop.
    return await _action(mavsdk_thread.drone.action.arm())


@app.post("/takeoff")
async def takeoff():
    return await _action(mavsdk_thread.drone.action.takeoff())


@app.post("/land")
async def land():
    return await _action(mavsdk_thread.drone.action.land())


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
