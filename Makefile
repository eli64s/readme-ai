# Makefile

COMMITS := 10
SHELL := /bin/bash
VENV := readmeai
VV := \

.PHONY: help clean format lint conda-recipe git-rm-cache git-log nox pytest poetry-reqs search

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "conda-recipe : builds conda package."
	@echo "git-rm-cache : fix git untracked files."
	@echo "git-log      : displays git log."
	@echo "nox          : executes nox test suite."
	@echo "pytest       : executes tests."
	@echo "poetry-reqs  : generates requirements.txt file."
	@echo "search       : searches word in directory."

.PHONY: clean
clean: format
	@echo -e "\nFile clean up in directory: ${CURDIR}"
	./scripts/clean.sh clean

.PHONY: format
format:
	@echo -e "\nFormatting in directory: ${CURDIR}"
	ruff check --select I --fix .
	ruff format .

.PHONY: lint
lint:
	@echo -e "\nLinting in directory: ${CURDIR}"
	ruff check . --fix

.PHONY: conda-recipe
conda-recipe:
	grayskull pypi readmeai
	conda build .

.PHONY: git-rm-cache
git-rm-cache:
	git rm -r --cached .

.PHONY: git-log
git-log:
	git log -n ${COMMITS} --pretty=tformat: --shortstat

.PHONY: nox
nox:
	nox -f noxfile.py

.PHONY: pytest
pytest:
	pytest ${VV} \
	-n auto \
	--asyncio-mode=auto \
	--cov=. \
	--cov-report=xml \
	--cov-report=term-missing \
	--cov-branch \

.PHONY: poetry-reqs
poetry-reqs:
	poetry export -f requirements.txt --output setup/requirements.txt --without-hashes

.PHONY: search
search: clean
	@echo -e "\nSearching for: ${WORD} in directory: ${CURDIR}"
	grep -Ril ${WORD} readmeai tests scripts setup
