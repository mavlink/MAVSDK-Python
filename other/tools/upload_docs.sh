#!/usr/bin/env bash

# Helper to upload artifact to s3 and set permissions and metadata correct.
# http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/

# Sync everything
s3cmd sync mavsdk/build/html/ s3://mavsdk-python-docs

# Fix meta data
s3cmd put -m text/html mavsdk/build/html/index.html s3://mavsdk-python-docs

s3cmd put -m text/javascript mavsdk/build/html/searchindex.js s3://mavsdk-python-docs
s3cmd put -m text/javascript mavsdk/build/html/_static/jquery.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/doctools.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/underscore.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/documentation_options.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/javascript mavsdk/build/html/_static/language_data.js s3://mavsdk-python-docs/_static/
s3cmd put -m text/css mavsdk/build/html/_static/nature.css s3://mavsdk-python-docs/_static/
s3cmd put -m text/css mavsdk/build/html/_static/basic.css s3://mavsdk-python-docs/_static/

s3cmd put -m image/x-icon mavsdk/build/html/_static/favicon.png s3://mavsdk-python-docs/

# Set it all to public
s3cmd setacl -r s3://mavsdk-python-docs --acl-public
