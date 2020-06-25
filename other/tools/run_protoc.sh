#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../../"
PROTO_DIR="${WORK_DIR}/proto"
GENERATED_DIR="${WORK_DIR}/mavsdk"
TEMPLATE_PATH="${WORK_DIR}/other/templates/py"

TEMPLATE_PATH_RST="${WORK_DIR}/other/templates/rst"
GENERATED_DIR_RST="${WORK_DIR}/mavsdk/source/plugins"

PLUGIN_LIST=$(cd ${WORK_DIR}/proto/protos && ls -d */ | sed 's:/*$::')

command -v protoc-gen-mavsdk > /dev/null || {
    echo "-------------------------------"
    echo " Error"
    echo "-------------------------------"
    echo >&2 "'protoc-gen-mavsdk' not found in PATH"
    echo >&2 ""
    echo >&2 "Make sure 'protoc-gen-mavsdk' is installed and available"
    exit 1
}

function snake_case_to_camel_case {
    echo $1 | sed -r 's/(^|_)([a-z])/\U\2/g'
}

function generate {
    # Generate our extensions
    python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                 --python_out=${GENERATED_DIR} \
                                 --grpc_python_out=${GENERATED_DIR} \
                                 mavsdk_options.proto

    for plugin in ${PLUGIN_LIST}; do

        # Generate protobuf and gRPC files
        python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                     --python_out=${GENERATED_DIR} \
                                     --grpc_python_out=${GENERATED_DIR} \
                                     ${plugin}/${plugin}.proto

        # We need to create the .original backup files, otherwise we're not compatible with
        # BSD sed.
        sed -i'.sedoriginal' -e "s/import mavsdk_options_pb2/from . import mavsdk_options_pb2/" \
            "${GENERATED_DIR}/${plugin}/${plugin}_pb2.py"
        sed -i'.sedoriginal' -e "s/from ${plugin} import ${plugin}_pb2/from . import ${plugin}_pb2/" \
            "${GENERATED_DIR}/${plugin}/${plugin}_pb2_grpc.py"
        # Clean up the backup files.
        find ${GENERATED_DIR} -name '*.sedoriginal' -delete

        mv "${GENERATED_DIR}/${plugin}/${plugin}_pb2.py" "${GENERATED_DIR}/${plugin}_pb2.py"
        mv "${GENERATED_DIR}/${plugin}/${plugin}_pb2_grpc.py" "${GENERATED_DIR}/${plugin}_pb2_grpc.py"


        echo " -> [+] Generated protobuf and gRPC bindings for ${plugin}"

        # Generate plugin
        python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                     --plugin=protoc-gen-custom=$(which protoc-gen-mavsdk) \
                                     --custom_out=${GENERATED_DIR} \
                                     --custom_opt="file_ext=py,template_path=${TEMPLATE_PATH}" \
                                     ${plugin}/${plugin}.proto

        # protoc-gen-mavsdk capitalizes filenames, and we don't want that with python
        mv ${GENERATED_DIR}/${plugin}/$(snake_case_to_camel_case ${plugin}).py ${GENERATED_DIR}/${plugin}.py

        # Generate plugin doc entry
        python3 -m grpc_tools.protoc -I${PROTO_DIR}/protos \
                                     --proto_path=${PROTO_DIR}/protos/${plugin} \
                                     --plugin=protoc-gen-custom=$(which protoc-gen-mavsdk) \
                                     --custom_out=${GENERATED_DIR_RST} \
                                     --custom_opt="file_ext=rst,template_path=${TEMPLATE_PATH_RST}" \
                                     ${plugin}.proto

        # Again move generated file to its place.
        mv ${GENERATED_DIR_RST}/$(snake_case_to_camel_case ${plugin}).rst ${GENERATED_DIR_RST}/${plugin}.rst
        echo " -> [+] Generated doc entry for ${plugin}"

        # Add plugin entry to docs index if not already listed.
        if [[ ! $(grep ${plugin} ${GENERATED_DIR_RST}/index.rst) ]]; then
            echo " -> [+] Add doc entry for ${plugin} to index"
            echo "   ${plugin}" >> ${GENERATED_DIR_RST}/index.rst
        fi

        rmdir ${GENERATED_DIR}/${plugin}

    done
}

echo "[+] Generating plugins from "
generate
echo "[+] Done"
