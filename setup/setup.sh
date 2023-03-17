#!/bin/bash

# Create conda environment
conda create --name readmeai python=3.9 -y

# Activate conda environment
eval "$(conda shell.bash hook)"
conda activate readmeai

# Install project dependencies
pip install -e .

# Download spacy language model
python -m spacy download en_core_web_sm
