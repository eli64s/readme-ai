# Makefile

SHELL = /bin/bash
VENV := readmeai

.PHONY: help clean format lint reqs conda venv git-rm-cache test

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "reqs         : installs requirements."
	@echo "conda        : creates a conda environment."
	@echo "venv         : creates a virtual environment."
	@echo "git-rm-cache : fix git untracked files."
	@echo "test         : executes tests."

.PHONY: clean
clean: format
	bash scripts/clean.sh clean

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
	conda create -f setup/environment.yml

.PHONY: venv
venv:
	python -m venv $(VENV) && \
	source $(VENV)/bin/activate && \
	$(MAKE) reqs

.PHONY: git-rm-cache
git-rm-cache:
	git rm -r --cached .

.PHONY: test
test:
	bash scripts/test.sh
