#!/usr/bin/env bash

# Function to check if a conda environment exists
function conda_env_exists() {
    local env_name="$1"
    conda activate "$env_name" &> /dev/null
    local activated=$?
    conda deactivate &> /dev/null
    return $activated
}

# Install tree command if it's not installed
if ! command -v tree &> /dev/null
then
    if [ "$(uname)" == "Darwin" ]; then
        # macOS
        brew install tree
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        # Linux
        if [ -x "$(command -v apt-get)" ]; then
            # Debian/Ubuntu
            sudo apt-get update && sudo apt-get install tree
        elif [ -x "$(command -v yum)" ]; then
            # CentOS
            sudo yum install tree
        elif [ -x "$(command -v pacman)" ]; then
            # Arch Linux
            sudo pacman -S tree
        elif [ -x "$(command -v zypper)" ]; then
            # OpenSUSE
            sudo zypper install tree
        else
            echo "Your Linux distribution's package manager is not supported. Please install 'tree' manually."
            exit 1
        fi
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
        # Windows
        choco install tree
    fi
fi

# Welcome message
echo "Welcome to the README-AI environment setup script!"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and rerun the script."
    exit 1
fi

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Conda is not installed. Please install Anaconda or Miniconda and rerun the script."
    exit 1
fi

# Check for Python installation and required version (3.7+)
echo "Checking for Python 3.7 or higher..."
python_version=$(python3 -c 'import sys; print("{}.{}".format(sys.version_info[0], sys.version_info[1]))' 2>/dev/null)

if [ $? -ne 0 ]; then
    echo "Python 3 is not installed. Please install Python 3.7 or higher and rerun the script."
    exit 1
fi

IFS='.' read -ra version_parts <<< "$python_version"
major=${version_parts[0]}
minor=${version_parts[1]}

if [ "$major" -lt 3 ] || ([ "$major" -eq 3 ] && [ "$minor" -lt 7 ]); then
    echo "Please upgrade to Python 3.7 or higher and rerun the script."
    exit 1
fi

echo "Python version is compatible."

# Check if 'readmeai' environment already exists
if conda_env_exists "readmeai"; then
    echo "The 'readmeai' environment already exists. Skipping environment creation."
else
    # Create a new conda environment named 'readmeai'
    echo "Creating a new conda environment named 'readmeai' with Python 3.9..."
    conda create --name readmeai python=3.9 -y
fi

# Activate the conda environment
echo "Activating the 'readmeai' environment..."
eval "$(conda shell.bash hook)"
conda activate readmeai

# Check if Poetry is installed
echo "Checking if Poetry is installed..."
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
else
    echo "Poetry is already installed."
fi

# Change to the project directory
cd readme-ai

# Install project dependencies using Poetry
echo "Installing project dependencies with Poetry..."
poetry install

# Deactivate the conda environment
conda deactivate

echo "Setup complete. Use 'conda activate readmeai' to activate the environment."
