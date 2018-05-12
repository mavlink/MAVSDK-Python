#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WORK_DIR="${SCRIPT_DIR}/.."
SRC_DIR="${WORK_DIR}/src"

for PROTO_SUBDIR in `ls ${WORK_DIR}/proto`; do
    if [ ! -d ${WORK_DIR}/proto/${PROTO_SUBDIR} ]; then
        continue
    fi

    PACKAGE_NAME="dronecore_${PROTO_SUBDIR}"
    PACKAGE_DIR=${SRC_DIR}/${PACKAGE_NAME}/${PACKAGE_NAME}

    echo "Creating package directory '${PACKAGE_DIR}'..."
    mkdir -p ${PACKAGE_DIR}
    
    # For each component, copy the *.proto file into the package
    cp ${WORK_DIR}/proto/${PROTO_SUBDIR}/*.proto ${PACKAGE_DIR}

    # Generate the corresponding protobuf and grpc files
    python -m grpc_tools.protoc -I${SRC_DIR}/${PACKAGE_NAME} --python_out=${SRC_DIR}/${PACKAGE_NAME} --grpc_python_out=${SRC_DIR}/${PACKAGE_NAME} ${PACKAGE_DIR}/*.proto
done
