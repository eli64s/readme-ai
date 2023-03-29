#!/bin/bash

# Clone the repository
#echo "Cloning the README-AI repository..."
#git clone https://github.com/eli64s/README-AI.git
#cd README-AI

# Welcome message
echo "Welcome to the README-AI environment setup script!"

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Anaconda or Miniconda and rerun the script."
    exit 1
fi

# Check for Python installation and required version (3.7+)
echo "Checking for Python 3.7 or higher..."
python_version=$(python3 -c 'import sys; print(sys.version_info[:])' 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "Python 3 is not installed. Please install Python 3.7 or higher and rerun the script."
    exit 1
fi

if [ ${python_version:1:1} -lt 3 ] || ([ ${python_version:1:1} -eq 3 ] && [ ${python_version:4:1} -lt 7 ]); then
    echo "Please upgrade to Python 3.7 or higher and rerun the script."
    exit 1
fi

echo "Python version is compatible."

# Create a new conda environment named 'readmeai'
echo "Creating a new conda environment named 'readmeai' with Python 3.8..."
conda create -n readmeai python=3.8 -y

# Activate the conda environment
echo "Activating the 'readmeai' environment..."
eval "$(conda shell.bash hook)"
conda activate readmeai

# Install the required packages
echo "Installing required packages from 'requirements.txt'..."
pip install -r requirements.txt

echo "Packages installed successfully."

# Download spacy language model
echo "Downloading the spaCy language model 'en_core_web_sm'..."
python -m spacy download en_core_web_sm

# Deactivate the conda environment when setup is complete
conda deactivate

echo "Setup complete. Use 'conda activate readmeai' to activate the environment."