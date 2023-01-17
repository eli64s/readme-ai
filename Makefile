# Makefile
SHELL = /bin/bash

.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."

# Set api secret key for ChatGPT.
OPENAI_API_KEY=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
export OPENAI_API_KEY
api_key:
	echo "Set OPENAI_API_KEY"

# Automated docstring creation.
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
	-find . -name '*.log' -delete
	-find . -type f -name "*.DS_Store" -ls -delete
	-find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	-find . | grep -E ".pytest_cache" | xargs rm -rf
	-find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	-find . | grep -E ".trash" | xargs rm -rf
	-rm -f .coverage
	-rm -rf UNKNOWN.egg-info
	-rm -rf _tmp
	-rm -rf outputs

# Conda Virtual Environment
conda:
	conda create -n $(ARG) python=3.9 pip conda -y
	source activate $(ARG) && \
	pip install -r requirements.txt
