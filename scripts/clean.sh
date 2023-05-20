#!/bin/bash

# Remove backup files and Python cache files
find . -type f \( -name "*.py-e" \
                  -o -name "*.DS_Store" \
                  -o -name "*.py[co]" \) -delete

# Remove cache directories and VS Code settings
find . -type d \( -name "__pycache__" \
                  -o -name ".ipynb_checkpoints" \
                  -o -name ".ruff_cache" \
                  -o -name ".vscode" \) -execdir rm -rf {} +

# Remove build artifacts, pytest cache, and benchmarks
rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .benchmarks/

# Remove specific files
rm -rf docs/raw_data.csv *.log *.out *.rdb
