#!/bin/bash

# Check if Conda is already installed
if command -v conda >/dev/null 2>&1; then
    echo "Conda is already installed."
else
    # Download and install Conda
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        wget -qO- https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh | bash
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        curl -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
        bash miniconda.sh -b -p $HOME/miniconda
    else
        echo "Unsupported operating system."
        exit 1
    fi
fi

# Update Conda
conda update -y conda

# Create conda environment
conda create -n readmeai python=3.9 -y

# Activate conda environment
eval "$(conda shell.bash hook)"
conda activate readmeai

# Install project dependencies
pip install -e .

# Download spacy language model
python -m spacy download en_core_web_sm