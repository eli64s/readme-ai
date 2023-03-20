#!/bin/bash

# Clean up Python cache files
find . -type f -name "*.DS_Store" -ls -delete
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove build artifacts
rm -rf build/ dist/ *.egg-info/

# Remove Jupyter notebook checkpoints
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

# Remove pytest cache
rm -rf .pytest_cache/
