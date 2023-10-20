# Makefile

SHELL = /bin/bash
VENV := readmeai

.PHONY: help clean format lint reqs conda venv git-rm-cache

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "reqs         : installs requirements."
	@echo "conda        : creates a conda environment."
	@echo "venv         : creates a virtual environment."
	@echo "git-rm-cache : fix git untracked files."

.PHONY: clean
clean: format
	bash scripts/clean.sh

.PHONY: format
format:
	-black .
	-isort .

.PHONY: lint
lint:
	-flake8 ${CURDIR}
	-ruff ${CURDIR}

.PHONY: reqs
reqs:
    pip install -r requirements.txt

.PHONY: conda
conda:
	conda create -n $(VENV) python=3.10 pip -y &&
	conda activate $(VENV) &&
	$(MAKE) reqs

.PHONY: venv
venv:
	python -m venv $(VENV) && \
	source $(VENV)/bin/activate && \
	$(MAKE) reqs

git-rm-cache:
	git rm -r --cached .
