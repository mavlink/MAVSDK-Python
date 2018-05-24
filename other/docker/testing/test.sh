#!/bin/sh

# We do NOT want to test in the actual mountpoint, therefore create a copy!
cp -Rf /src /srccopy && cd /srccopy

# Run tox for testing
tox --skip-missing-interpreters
