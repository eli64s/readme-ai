# Makefile
SHELL = /bin/bash

.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."

#export OPENAI_API_KEY=
api_key:
	echo "Set OPENAI_API_KEY"

# Automated docstrings
autodocs: api_key
	autodocstrings src

# Style
.PHONY: style
style:
	-black .
	-flake8
	-isort .

# Clean
.PHONY: clean
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
	conda create -n myenv python=3.9 pip conda -y
	source activate myenv && \
	pip install -r requirements.txt
