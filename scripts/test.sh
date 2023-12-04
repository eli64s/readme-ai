#!/usr/bin/env bash

eval "$(conda shell.bash hook)"
conda activate readmeai

source_dir="readmeai"
omit_dir="tests"
omit_file="readmeai/__init__.py,readmeai/*/__init__.py"

# Generate the coverage report and save it to a file
#pytest --cov=./ --cov-report=xml
coverage run --source="$source_dir" --omit="$omit_dir" --omit="$omit_file" -m pytest -v
coverage report --show-missing --fail-under=90
