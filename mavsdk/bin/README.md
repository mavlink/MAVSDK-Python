The gRPC server executable `mavsdk_server` (or `mavsdk_server.exe` on Windows) is placed here before packaging.

The canonical `hatch run build` workflow runs `hatch run download-server`, which first copies a locally built
server found below `MAVSDK_CPP_PROJECT_ROOT`. If no local server is found, it downloads the upstream release
selected by `MAVSDK_SERVER_VERSION`. The executable is included in the wheel as a Hatch build artifact.
