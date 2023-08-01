#!/usr/bin/env bash

set -e

bash scripts/clean.sh

python -m build

twine upload --verbose --repository-url https://upload.pypi.org/legacy/ -u __token__ -p $PYPI_API_KEY dist/*

echo "Successfully pushed new readmeai package to PyPI!"
