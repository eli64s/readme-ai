# Makefile

SHELL = /bin/bash
VENV := readmeai

.PHONY: help clean format lint build-conda git-rm-cache file-search test

help:
	@echo "Commands:"
	@echo "clean        : repository file cleanup."
	@echo "format       : executes code formatting."
	@echo "lint         : executes code linting."
	@echo "build-conda  : builds conda package."
	@echo "git-rm-cache : fix git untracked files."
	@echo "file-search  : search for text in files."
	@echo "test         : executes tests."

.PHONY: clean
clean: format
	./scripts/clean.sh clean

.PHONY: format
format:
	-black .
	-isort .

.PHONY: lint
lint:
	-flake8 ${CURDIR}
	-ruff ${CURDIR}

.PHONY: build-conda
build-conda:
	grayskull pypi readmeai
	conda build -c conda-forge -c pytorch -c anaconda -c defaults .

.PHONY: git-rm-cache
git-rm-cache:
	git rm -r --cached .

.PHONY: file-search
file-search:
	grep -R "ENTRYPOINT" .

.PHONY: test
test:
	pytest \
	--cov=./ \
	--cov-report=xml \
	--cov-report=term-missing
