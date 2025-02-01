#!/usr/bin/env python3

import asyncio
import base64
from mavsdk import System
from mavsdk.rtk import RtcmData


async def send_data(data):
    drone = System()
    await drone.connect()
    await drone.rtk.send_rtcm_data(data)


if __name__ == '__main__':
    rtcm_data = bytearray(b'\xd3\x00mCP\x00\x8c2\x16\x82\x00\x00,@\x88\x00\x00\x00\x00\x00 \x00\x00\x00~\x9c\xa4\x9a\x90\xa2\x8c\x00\x00\x01\xa7\xa2\x1e=gv\x8f\x1fq{\\x13_\xc9\xdf\x17\x02L$\xb6\xdd\x17\x9a.\xe8\xba\x94\x02U6^\xa2^\x08\xac\xf5\xf4\x1d\xcc\n\x9d\xe7\xeb\x04R\x15\x92\x93\xf9o\xf2\xc1\xb5-j\xba\xf12`@\r\x83\xc0\xe8B\x0f\x05\xec\x8c\xfc\xc4\x88l\xac\x7f\xf1\x1aR\xc2\xbc\x87')  # noqa: E501
    # In MAVSDK 3.0.0 the data is expected to be base64 encoded string
    base64_rtcm_data = base64.b64encode(rtcm_data).decode('utf-8')
    asyncio.run(send_data(RtcmData(base64_rtcm_data)))
