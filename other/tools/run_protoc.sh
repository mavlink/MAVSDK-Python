#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../.."
PROTO_DIR="${WORK_DIR}/proto/"
GENERATED_DIR="${WORK_DIR}/dronecode_sdk/generated"
PLUGIN_DIR="${WORK_DIR}/dronecode_sdk/plugins"

function generate {
    for PROTO_FILE in `find ${PROTO_DIR} -name "*.proto" -type f`; do

        # Generate bindings for each file individually
        protoc -I${GENERATED_DIR} \
               --proto_path=$(dirname ${PROTO_FILE}) \
               --python_out=${GENERATED_DIR} \
               --grpc_python_out=${GENERATED_DIR} \
               ${PROTO_FILE}

        # For some reason the import is broken with Python3.5.x and works fine
        # with Python3.6.x, set an absolute path and everything is fine
        PROTO_IMPORT_NAME="$(basename -- ${PROTO_FILE%.*})_pb2"
        sed "s/import ${PROTO_IMPORT_NAME}/from . import ${PROTO_IMPORT_NAME}/" \
             -i "${GENERATED_DIR}/${PROTO_IMPORT_NAME}_grpc.py"

        echo " -> [+] Generated protobuf and gRPC bindings for ${PROTO_IMPORT_NAME%_*}"

        
        # Generate plugin
        protoc --plugin=protoc-gen-custom=$(which dcsdkgen) \                        
            -I$(dirname ${PROTO_FILE}) \
            --custom_out=${PLUGIN_DIR} \
            --custom_opt=py \
            ${PROTO_FILE}
        echo " -> [+] Generated plugin for ${PROTO_IMPORT_NAME%_*}"

    done
}

function install_dcsdkgen {
    cd ${PROTO_DIR}/pb_plugins
    pip install -e .
}

echo "[+] Updating submodule"
cd $WORK_DIR
git submodule init
git submodule update --recursive
echo "[+] Done"
echo "[+] Installing the DronecodeSDK autogenerator"
install_dcsdkgen
echo "[+] Done"
echo "[+] Generating plugins from "
generate
echo "[+] Done"
