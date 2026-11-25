import asyncio
import subprocess
from unittest import mock

import pytest

from mavsdk import system


@pytest.fixture
def started_servers():
    """Patch out mavsdk_server and plugin init; record each server start."""
    calls = []

    def fake_start(system_address, port, sysid, compid):
        calls.append(
            {"system_address": system_address, "port": port, "sysid": sysid, "compid": compid}
        )
        return mock.MagicMock(spec=subprocess.Popen)

    with mock.patch.object(system.System, "_start_mavsdk_server", staticmethod(fake_start)):
        with mock.patch.object(system.System, "_init_plugins", mock.AsyncMock()):
            with mock.patch.object(system.asyncio, "sleep", mock.AsyncMock()):
                yield calls


def test_reconnect_keeps_sysid_compid_and_port(started_servers):
    drone = system.System(port=50060, sysid=1, compid=191)

    async def connect_twice():
        await drone.connect(system_address="udpin://0.0.0.0:14540")
        await drone.connect(system_address="udpin://0.0.0.0:14541")

    asyncio.run(connect_twice())

    assert started_servers == [
        {"system_address": "udpin://0.0.0.0:14540", "port": 50060, "sysid": 1, "compid": 191},
        {"system_address": "udpin://0.0.0.0:14541", "port": 50060, "sysid": 1, "compid": 191},
    ]


def test_reconnect_kills_previous_server(started_servers):
    drone = system.System()

    asyncio.run(drone.connect())
    first_server = drone._server_process
    asyncio.run(drone.connect())

    first_server.kill.assert_called_once()
    assert drone._server_process is not first_server
    assert len(started_servers) == 2


def test_external_server_is_not_started_or_stopped(started_servers):
    drone = system.System(mavsdk_server_address="192.168.1.10", port=50051)

    asyncio.run(drone.connect())
    asyncio.run(drone.connect())

    assert started_servers == []
    assert drone._mavsdk_server_address == "192.168.1.10"
