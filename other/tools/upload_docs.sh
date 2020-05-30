#!/usr/bin/env bash

# Helper to upload artifact to s3 and set permissions and metadata correct.
# http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/

# Sync everything
s3cmd sync mavsdk/build/html/genindex.html mavsdk/build/html/_images mavsdk/build/html/index.html mavsdk/build/html/objects.inv mavsdk/build/html/plugins mavsdk/build/html/py-modindex.html mavsdk/build/html/search.html mavsdk/build/html/searchindex.js mavsdk/build/html/_sources mavsdk/build/html/_static mavsdk/build/html/system.html s3://mavsdk-python-docs

# Fix meta data
s3cmd put -m text/html mavsdk/build/html/index.html s3://mavsdk-python-docs

s3cmd put -m text/javascript mavsdk/build/html/searchindex.js s3://mavsdk-python-docs
s3cmd put -m text/javascript mavsdk/build/html/_static/jquery.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/doctools.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/underscore.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/documentation_options.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/language_data.js s3://mavsdk-python-docs/_static/

# Set it all to public
s3cmd setacl -r s3://mavsdk-python-docs --acl-public
