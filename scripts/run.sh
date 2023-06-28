#!/usr/bin/env bash

set -eo pipefail

# If you need to export environment variables, do it here
# export OPENAI_API_KEY=""

# Activate the conda environment
eval "$(conda shell.bash hook)"
conda activate readme_ai

# Run the Python script
python src/main.py
