#!/usr/bin/env bash

set -eo pipefail

# If you need to export environment variables, do it here
# export OPENAI_API_KEY=""

# Activate the conda environment
eval "$(conda shell.bash hook)"
conda activate readmeai

# Run the Python script
python -m readmeai.cli -o readme-ai.md -r https://github.com/eli64s/readme-ai
