COMMITS := 10
SHELL := /bin/bash
SRC_PATH := readmeai
TEST_PATH := tests
VENV := readmeai

.PHONY: clean
clean: ## Remove project build artifacts
	./scripts/clean.sh clean

.PHONY: conda-recipe
conda-recipe: ## Create conda recipe for conda-forge
	grayskull pypi readmeai
	conda build .

.PHONY: docker-build
docker-build: ## Build Docker image for application
	docker build -t zeroxeli/readme-ai:latest .

.PHONY: git-log
git-log: ## Display git log for last 'N' commits
	git log -n ${COMMITS} --pretty=tformat: --shortstat

.PHONY: git-rm-cache
git-rm-cache: ## Remove all files from git cache
	git rm -r --cached .

.PHONY: poetry-clean
poetry-clean: ## Removes Poetry virtual environment and lock file.
	poetry env remove --all && rm poetry.lock

.PHONY: poetry-install
poetry-install: ## Install dependencies using Poetry.
	poetry install

.PHONY: poetry-shell
poetry-shell: ## Launch a shell within Poetry virtual environment.
	poetry shell

.PHONY: poetry-to-requirements
poetry-to-reqs: ## Export poetry requirements to requirements.txt
	poetry export -f requirements.txt --output setup/requirements.txt --without-hashes

.PHONY: ruff-format
ruff-format: ## Format codebase using Ruff
	ruff check --select I --fix .
	ruff format .

.PHONY: ruff-lint
ruff-lint: ## Lint codebase using Ruff
	ruff check . --fix

.PHONY: run-docs
run-docs: ## Run the MkDocs server
	mkdocs serve

.PHONY: search
search: ## Search for a word in the codebase
	grep -Ril ${WORD} readmeai tests scripts setup

.PHONY: test
test: ## Run unit tests using pytest
	poetry run pytest

.PHONY: test-nox
test-nox: ## Run test suite against multiple Python versions
	nox -f noxfile.py

.PHONY: help
help: Makefile ## Display the help menu
	@echo -e ""
	@echo -e "Usage: make [target]"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo -e "__________________________________________________________________________________________\n"
