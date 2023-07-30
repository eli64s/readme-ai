#!/usr/bin/env bash

eval "$(conda shell.bash hook)"
conda activate readmeai

# Set the directories to include in the coverage report
source_dir="readmeai"

# Set the directories to exclude from the coverage report
omit_dir="tests"

# Exclude __init__.py specifically
omit_file="readmeai/__init__.py"

# Generate the coverage report and save it to a file
coverage run --source="$source_dir" --omit="$omit_dir" --omit="$omit_file" -m pytest
coverage report --show-missing --fail-under=90

# Remove files and folders
find . -type d -name "__pycache__" -exec rm -r {} +
rm -rf .pytest_cache
rm -rf .coverage
rm -rf tests/*local_dir*
