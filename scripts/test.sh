#!/usr/bin/env bash

eval "$(conda shell.bash hook)"
conda activate readmeai

source_dir="readmeai"
omit_dir="tests"
omit_file="readmeai/__init__.py,readmeai/*/__init__.py"

# pytest --cov=./ --cov-report=xml --cov-report=term-missing --cov-fail-under=100
coverage run --source="$source_dir" --omit="$omit_dir" --omit="$omit_file" -m pytest -v
coverage report --show-missing --fail-under=90
