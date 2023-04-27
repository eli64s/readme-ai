#!/bin/bash

# Backup files
find . -type f -name "*.py-e" -delete

# Clean up Python cache files
find . -type f -name "*.DS_Store" -ls -delete
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -exec rm -rf {} +
find src -type d -name "__pycache__" -exec rm -r {} \;

# Remove build artifacts
rm -rf build/ dist/ *.egg-info/

# Remove Jupyter notebook checkpoints
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

# Remove pytest cache
rm -rf .pytest_cache/

# Remove benchmarks
rm -rf .benchmarks/

# Remove docs/raw_data.csv
rm -rf docs/raw_data.csv
