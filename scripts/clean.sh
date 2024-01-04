#!/usr/bin/env bash

function clean() {
    clean_build
    clean_pyc
    clean_test
    clean_backup_and_cache
    echo "All build, test, coverage, and Python artifacts have been removed."
}

function clean_build() {
    echo "Removing build artifacts..."
    rm -fr build/
    rm -fr dist/
    rm -fr .eggs/
    rm -fr site/
    rm -fr .p
    find . -name '*.egg-info' -exec rm -fr {} +
    find . -name '*.egg' -exec rm -f {} +
}

function clean_pyc() {
    echo "Removing Python file artifacts..."
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +
    find . -name '__pycache__' -exec rm -fr {} +
}

function clean_test() {
    echo "Removing test and coverage artifacts..."
    rm -f .coverage coverage.*
    rm -fr .nox/
    rm -fr .tox/
    rm -fr htmlcov/
    rm .coverage
    rm coverage.xml
}

function clean_backup_and_cache() {
    echo "Removing backup files and Python cache files..."
    rm -fr .mypy_cache/
    rm -fr .pytest_cache/
    find . -type f \( -name "*.py-e" \
                      -o -name "*.DS_Store" \
                      -o -name "*.py[co]" \) -delete
    echo "Removing cache directories and VS Code settings..."
    find . -type d \( -name "__pycache__" \
                      -o -name ".ipynb_checkpoints" \
                      -o -name ".ruff_cache" \
                      -o -name ".vscode" \) -execdir rm -rf {} +
}

# Check for command line arguments
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <command>"
    echo "Available commands: clean, clean-build, clean-pyc, clean-test, clean-backup-and-cache"
    exit 1
fi

case "$1" in
    clean)
        clean
        ;;
    clean-build)
        clean_build
        ;;
    clean-pyc)
        clean_pyc
        ;;
    clean-test)
        clean_test
        ;;
    clean-backup-and-cache)
        clean_backup_and_cache
        ;;
    *)
        echo "Unknown command: $1"
        echo "Available commands: clean, clean-build, clean-pyc, clean-test, clean-backup-and-cache"
        exit 1
        ;;
esac
