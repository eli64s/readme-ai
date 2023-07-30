# Makefile

SHELL = /bin/bash
VENV := readmeai

.PHONY: help style clean conda venv git-fix

help:
	@echo "Commands:"
	@echo "clean      : cleans all unnecessary files."
	@echo "style      : executes style formatting."
	@echo "conda      : creates a conda environment."
	@echo "venv       : creates a virtual environment."
	@echo "git-fix    : fix git untracked files."

.PHONY: style
style:
	-ruff .
	-black .
	-flake8
	-python3 -m isort .

.PHONY: clean
clean: style
	bash scripts/clean.sh

conda:
	conda create -n $(VENV) python=3.10 -y
	conda activate $(VENV) && pip install -r setup/requirements.txt

venv:
	python -m venv $(VENV)
	source $(VENV)/bin/activate
	pip install -r setup/requirements.txt

git-fix:
	git rm -r --cached .
	git add .
	git commit -m "Fix untracked project files."
