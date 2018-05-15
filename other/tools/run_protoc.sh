#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/../.."
PROTO_DIR="${WORK_DIR}/proto/"
GENERATED_DIR="${WORK_DIR}/dronecore/generated"

function generate {
    for PROTO_FILE in `find ${PROTO_DIR} -name "*.proto" -type f`; do

        # Generate bindings for each file individually
        python -m grpc_tools.protoc --proto_path=$(dirname ${PROTO_FILE}) \
                                    --python_out=${GENERATED_DIR} \
                                    ${PROTO_FILE}

    done
}

echo "[+] Generating protobuf and gRPC bindings"
generate
