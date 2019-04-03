It is expected that the grpc server binary `backend_bin` is present here when the wheel is built with:

    python setup.py bdist_wheel

The binary will not be versioned, so that should probably be done by the CI.
