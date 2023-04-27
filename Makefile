SHELL = /bin/bash
VENV := readmeai

.PHONY: help style clean conda venv

# Help
help:
	@echo "Commands:"
	@echo "clean   : cleans all unnecessary files."
	@echo "style   : executes style formatting."
	@echo "conda   : creates a conda environment."
	@echo "venv    : creates a virtual environment."

# Style
.PHONY: style
style:
	-black .
	-flake8
	-isort .

# Clean
.PHONY: clean
clean: style
	bash scripts/clean.sh

# Conda Environment
conda:
	conda create -n $(VENV) python=3.9 -y
	conda activate $(VENV) && pip install -r requirements.txt

# Python Virtual Environment
venv:
	python -m venv $(VENV)
	source venv/bin/activate
	pip install -r requirements.txt
