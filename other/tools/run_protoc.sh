#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../../"
PROTO_DIR="${WORK_DIR}/proto"
GENERATED_DIR="${WORK_DIR}/dronecode_sdk/generated"
PLUGIN_DIR="${WORK_DIR}/dronecode_sdk/plugins"
PLUGIN_INIT="${PLUGIN_DIR}/__init__.py"
export TEMPLATE_PATH="${WORK_DIR}/other/templates/"

function generate {
    echo -e "# -*- coding: utf-8 -*-\n" > $PLUGIN_INIT

    for PROTO_FILE in `find ${PROTO_DIR} -name "*.proto" -type f`; do

        # Generate bindings for each file individually
        python3 -m grpc_tools.protoc -I${GENERATED_DIR} \
                                     --proto_path=$(dirname ${PROTO_FILE}) \
                                     --python_out=${GENERATED_DIR} \
                                     --grpc_python_out=${GENERATED_DIR} \
                                     ${PROTO_FILE}

        # For some reason the import is broken with Python3.5.x and works fine
        # with Python3.6.x, set an absolute path and everything is fine
        PROTO_IMPORT_NAME="$(basename -- ${PROTO_FILE%.*})_pb2"

        # We need to create the .original backup files, otherwise we're not compatible with
        # BSD sed.
        sed -i'.sedoriginal' -e "s/import ${PROTO_IMPORT_NAME}/from . import ${PROTO_IMPORT_NAME}/" \
            "${GENERATED_DIR}/${PROTO_IMPORT_NAME}_grpc.py"
        # Clean up the backup files.
        find ${GENERATED_DIR} -name '*.sedoriginal' -delete

        echo " -> [+] Generated protobuf and gRPC bindings for ${PROTO_IMPORT_NAME%_*}"

        # Generate plugin
        python3 -m grpc_tools.protoc -I$(dirname ${PROTO_FILE}) \
                                     --plugin=protoc-gen-custom=$(which dcsdkgen) \
                                     --custom_out=${PLUGIN_DIR} \
                                     --custom_opt=py \
                                     ${PROTO_FILE}

        WANTED_PLUGIN_NAME="$(echo ${PROTO_FILE} | sed "s#.*/\(.*\).proto#\1#g").py"
        # protoc generates java like filenames, we don't want that with python

        # @TODO: cleanup this script and figure out a way to make it cross-os friendly perhaps rewrite in python
        # capilalization as trivial as this needs a workaround for macos bash 3.2
        # this solution avoids using bash ^ substitution (from bash >4.0) and is using python 3 instead
        CAPITALIZED_PLUGIN_NAME=$(python3 -c "import sys;print(sys.argv[1].capitalize())" "$WANTED_PLUGIN_NAME")
        mv ${PLUGIN_DIR}/${CAPITALIZED_PLUGIN_NAME} ${PLUGIN_DIR}/${WANTED_PLUGIN_NAME}

        # Add to imports
        echo "from .${WANTED_PLUGIN_NAME%.py} import *" >> $PLUGIN_INIT
        echo " -> [+] Generated plugin for ${PROTO_IMPORT_NAME%_*}"

    done
}

function install_dcsdkgen {
    cd ${PROTO_DIR}/pb_plugins
    if [[ "$VIRTUAL_ENV" != "" ]]
    then
        pip3 install .
    else
        pip3  install --user .
    fi
}

echo "[+] Installing the DronecodeSDK autogenerator"
install_dcsdkgen
echo "[+] Done"
echo "[+] Generating plugins from "
generate
echo "[+] Done"
