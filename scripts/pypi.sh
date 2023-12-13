#!/usr/bin/env bash
set -e

# Config
PACKAGE="readmeai"
REPOSITORY="https://upload.pypi.org/legacy/"
USERNAME="__token__"
API_KEY="$PYPI_API_KEY"

# Helper functions
function clean {
    bash scripts/clean.sh
}

function build {
    python -m build
}

function upload {
    twine upload --verbose \
    --repository-url "$REPOSITORY" \
    --username "$USERNAME" \
    --password "$API_KEY" \
    dist/*
}

function main {

    clean
    build

    echo "Uploading $PACKAGE distribution files"
    upload

    echo "Successfully deployed new version of $PACKAGE to PyPI"
}

main
