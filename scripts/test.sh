#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate readmeai

# Set the directories to include in the coverage report
source_dir="src"

# Set the directories to exclude from the coverage report
omit_dir="tests, src/__init__.py"

# Generate the coverage report and save it to a file
coverage run --source="$source_dir" --omit="$omit_dir" -m pytest
coverage report --show-missing --fail-under=90

# Remove files and folders
find . -type d -name "__pycache__" -exec rm -r {} +
rm -rf .pytest_cache
rm -rf .coverage
