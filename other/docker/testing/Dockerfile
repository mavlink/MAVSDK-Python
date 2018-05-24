# Based on https://github.com/xvzf/tox-docker
FROM alpine:3.7

# Prefere local python binaries over the distributed ones
ENV PATH /usr/local/bin:$PATH

# Needed for Python 3
ENV LANG C.UTF-8

RUN apk add --no-cache ca-certificates

# Install requirements
RUN apk add --no-cache --virtual .fetch-deps \
        openssl \
        tar \
        xz \
    && apk add --no-cache --virtual .build-deps  \
        bzip2-dev \
        coreutils \
        dpkg-dev dpkg \
        expat-dev \
        gcc \
        gdbm-dev \
        libc-dev \
        libffi-dev \
        libnsl-dev \
        libtirpc-dev \
        linux-headers \
        make \
        ncurses-dev \
        openssl \
        openssl-dev \
        pax-utils \
        readline-dev \
        sqlite-dev \
        tcl-dev \
        tk \
        tk-dev \
        xz-dev \
        zlib-dev

# Copy build script
COPY build_python.sh /build_python.sh

# PYTHON VERSIONS
ENV PYTHON_VERSIONS 2.7.15 3.4.8 3.5.5 3.6.5
ENV PYTHON_PIP_VERSION 10.0.1

# Build python versions using the script
RUN sh -ex /build_python.sh

# Remove installed packages to keep the image as slim as possible
RUN apk del .fetch-deps \
    && apk del .build-deps \
    && rm /build_python.sh

# Some packages needed for cython
RUN apk add --no-cache \
    gcc \
    g++ \
    libc-dev \
    make \
    openssl \
    openssl-dev

# Installing tox for one python version is sufficient
RUN pip3.6 install tox

# Copy script for testing
COPY test.sh /test.sh

# Set ENTRYPOINT
ENTRYPOINT ["sh", "-ex", "/test.sh"]
