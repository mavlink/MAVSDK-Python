#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../../"
PROTO_DIR="${WORK_DIR}/proto"
GENERATED_DIR="${WORK_DIR}/mavsdk/generated"
PLUGIN_INIT="${GENERATED_DIR}/__init__.py"
export TEMPLATE_PATH="${WORK_DIR}/other/templates/py"

PLUGIN_LIST=$(cd ${WORK_DIR}/proto/protos && ls -d */ | sed 's:/*$::')

function snake_case_to_camel_case {
    echo $1 | sed -r 's/(^|_)([a-z])/\U\2/g'
}

function generate {
    printf "# -*- coding: utf-8 -*-\n\n" > $PLUGIN_INIT

    # Generate our extensions
    python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                 --proto_path=${PROTO_DIR}/protos/ \
                                 --python_out=${GENERATED_DIR} \
                                 --grpc_python_out=${GENERATED_DIR} \
                                 mavsdk_options.proto

    for plugin in ${PLUGIN_LIST}; do

       # Generate protobuf and gRPC files
        python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                     --proto_path=${PROTO_DIR}/protos/${plugin} \
                                     --python_out=${GENERATED_DIR} \
                                     --grpc_python_out=${GENERATED_DIR} \
                                     ${plugin}.proto

        # We need to create the .original backup files, otherwise we're not compatible with
        # BSD sed.
        sed -i'.sedoriginal' -e "s/import mavsdk_options_pb2/from . import mavsdk_options_pb2/" \
            "${GENERATED_DIR}/${plugin}_pb2.py"
        sed -i'.sedoriginal' -e "s/import ${plugin}_pb2/from . import ${plugin}_pb2/" \
            "${GENERATED_DIR}/${plugin}_pb2_grpc.py"
        # Clean up the backup files.
        find ${GENERATED_DIR} -name '*.sedoriginal' -delete

        echo " -> [+] Generated protobuf and gRPC bindings for ${plugin}"

        # Generate plugin
        python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                     --proto_path=${PROTO_DIR}/protos/${plugin} \
                                     --plugin=protoc-gen-custom=$(which protoc-gen-dcsdk) \
                                     --custom_out=${GENERATED_DIR} \
                                     --custom_opt=file_ext=py \
                                    ${plugin}.proto

        # protoc-gen-dcsdk capitalizes filenames, and we don't want that with python
        mv ${GENERATED_DIR}/$(snake_case_to_camel_case ${plugin}).py ${GENERATED_DIR}/${plugin}.py

        # Add to imports
        echo "from .${plugin} import *" >> $PLUGIN_INIT
        echo " -> [+] Generated plugin for ${plugin}"

    done
}

echo "[+] Generating plugins from "
generate
echo "[+] Done"
