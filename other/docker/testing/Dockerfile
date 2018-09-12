FROM ubuntu:18.04

# Prefere local python binaries over the distributed ones
ENV PATH /usr/local/bin:$PATH

# Needed for Python 3
ENV LANG C.UTF-8

RUN apt update \
    && apt-get --yes install tzdata \
    && ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && apt install --yes python python-dev python-pip wget\
                         python3 python3-dev python3-pip \
                         build-essential checkinstall python3-setuptools\
                         libreadline-gplv2-dev libncursesw5-dev zlib1g-dev\
                         libssl-dev libsqlite3-dev tk-dev python-smbus\
                         libgdbm-dev libc6-dev libbz2-dev libffi-dev\
    && rm -rf /var/lib/apt/lists/*

# Copy build script
COPY build_python.sh /build_python.sh

# PYTHON VERSIONS
ENV PYTHON_VERSIONS 3.7.0
ENV PYTHON_PIP_VERSION 10.0.1

# Build python versions using the script
 RUN bash -ex /build_python.sh

# Installing tox for one python version is sufficient
RUN pip3 install tox

# Copy script for testing
COPY test.sh /test.sh

# Set ENTRYPOINT
ENTRYPOINT ["sh", "-ex", "/test.sh"]
