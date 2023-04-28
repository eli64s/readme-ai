#!/bin/bash

# Remove unwanted files and directories

find . -type f -name "*.py-e" -delete # remove backup files
find . -type f -name "*.DS_Store" -ls -delete # remove Python cache files
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -exec rm -rf {} + # remove Python cache directories
find src -type d -name "__pycache__" -exec rm -r {} \;

rm -rf build/ dist/ *.egg-info/ # remove build artifacts
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + # remove Jupyter notebook checkpoints
rm -rf .pytest_cache/ # remove pytest cache
rm -rf .benchmarks/ # remove benchmarks
rm -rf docs/raw_data.csv # remove raw data file
rm -rf *.log *.out *.rdb # remove log files
