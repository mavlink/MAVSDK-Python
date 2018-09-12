#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../../"
PROTO_DIR="${WORK_DIR}/proto/"
GENERATED_DIR="${WORK_DIR}/dronecode_sdk/generated"
PLUGIN_DIR="${WORK_DIR}/dronecode_sdk/plugins"
TEMPLATE_PATH="${WORK_DIR}/other/templates/"

function generate {
    for PROTO_FILE in `find ${PROTO_DIR} -name "*.proto" -type f`; do

        # Generate bindings for each file individually
        python -m grpc_tools.protoc -I${GENERATED_DIR} \
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
        python -m grpc_tools.protoc -I$(dirname ${PROTO_FILE}) \
                                    --plugin=protoc-gen-custom=$(which dcsdkgen) \
                                    --custom_out=${PLUGIN_DIR} \
                                    --custom_opt=py \
                                    ${PROTO_FILE}
        WANTED_PLUGIN_NAME="$(echo ${PROTO_FILE} | sed "s#.*/\(.*\).proto#\1#g").py"
        mv ${PLUGIN_DIR}/${WANTED_PLUGIN_NAME^} ${PLUGIN_DIR}/${WANTED_PLUGIN_NAME}
        echo " -> [+] Generated plugin for ${PROTO_IMPORT_NAME%_*}"

    done
}

function install_dcsdkgen {
    cd ${PROTO_DIR}/pb_plugins
    pip install -e . > /dev/null
}

echo "[+] Installing the DronecodeSDK autogenerator"
install_dcsdkgen
echo "[+] Done"
echo "[+] Generating plugins from "
generate
echo "[+] Done"
