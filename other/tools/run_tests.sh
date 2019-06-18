#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../.."
DOCKER_DIR="${WORK_DIR}/other/docker/testing/"
DOCKER_IMAGE_NAME="tox-mavsdk-python"
DOCKER_BUILD_LOG_PATH="/tmp/mavsdk-python-docker-build.log"

function build_docker_image {
    cd $DOCKER_DIR
    echo "-> [+] Building the docker image used for testing multiple python versions (this can take some time)"
    docker build . -t $DOCKER_IMAGE_NAME &> $DOCKER_BUILD_LOG_PATH
    if [ $? -eq 0 ]; then
        echo "-> [+] Done!"
    else
        echo "-> [-] Failed to build the docker image, see ${DOCKER_BUILD_LOG_PATH}"
        exit 1
    fi
    cd $WORK_DIR
}

function run_tox {
    echo "-> [+] Running the test suite!"
    docker run --rm -v ${WORK_DIR}:/src $DOCKER_IMAGE_NAME
}

echo "[+] Building docker image"
build_docker_image

echo "[+] Running tests"
run_tox
