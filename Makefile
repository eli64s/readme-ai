#!/usr/bin/env make

SHELL := $(which bash)
VENV := myenv

.PHONY: help api_key autodocs style clean conda

# Help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."

# OpenAI API key
api_key:
ifndef OPENAI_API_KEY
	$(error OPENAI_API_KEY is undefined)
endif

# Style
style:
	-black .
	-flake8
	-isort .

# Clean
clean: style
	-rm -rf .vscode
	-find . -name '*.log' -delete
	-find . -type f -name "*.DS_Store" -ls -delete
	-find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	-find . | grep -E ".pytest_cache" | xargs rm -rf
	-find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	-find . | grep -E ".trash" | xargs rm -rf

# Conda Virtual Environment
conda:
	conda create -n $(VENV) python=3.9 -y
	conda activate $(VENV) && pip install -r requirements.txt
