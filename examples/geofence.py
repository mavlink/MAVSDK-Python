import asyncio

import mavsdk

mavsdk.start_mavlink(connection_url="udp//:14540")
drone = mavsdk.connect(host="127.0.0.1")

async def run():
    # pos = ()
    # async for npos in drone.telemetry.position():
        # pos = (npos.latitude_deg, npos.longitude_deg)
        # return
    # print(pos)
    # lat = pos.latitude_deg
    # lon = pos.longitude_deg
    # print(lat, lon)
    # 47.3977508, 8.5456074
    lat = 47.3977508
    lon = 8.5456074
    p1 = mavsdk.Point(lat - 0.0001, lon - 0.0001)
    p2 = mavsdk.Point(lat + 0.0001, lon - 0.0001)
    p3 = mavsdk.Point(lat + 0.0001, lon + 0.0001)
    p4 = mavsdk.Point(lat - 0.0001, lon + 0.0001)
    polygon = mavsdk.Polygon([p1, p2, p3, p4], mavsdk.Polygon.Type.INCLUSION)
    print(polygon)
    print("Uploading geofence...")
    await drone.geofence.upload_geofence([polygon])
    print("Uploaded")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
