SHELL = /bin/bash
VENV := readmeai

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
.PHONY: style
style:
	-black .
	-flake8
	-isort .

# Clean
.PHONY: clean
clean: style
	-rm -rf .vscode
	-rm -rf .ruff_cache
	-rm -rf readmeai.egg-info
	-find . -name '*.log' -delete
	-find . -type f -name "*.DS_Store" -ls -delete
	-find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	-find . | grep -E ".pytest_cache" | xargs rm -rf
	-find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	-find . | grep -E ".trash" | xargs rm -rf


# Conda virtual environment
conda:
	conda create -n $(VENV) python=3.9 -y
	conda activate $(VENV) && pip install -r requirements.txt

# Python virtual environment
venv: 
	python -m venv $(VENV)
	source venv/bin/activate
	pip install -r requirements.txt