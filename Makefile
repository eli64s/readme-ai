SHELL := /bin/bash
SRC_PATH := readmeai
TEST_PATH := tests

.PHONY: clean
clean: ## Remove project build artifacts
	./scripts/clean.sh clean_pyc

.PHONY: docker-build
docker-build: ## Build Docker image for application
	docker build -t zeroxeli/readme-ai:latest .

.PHONY: poetry-install
poetry-install: ## Install dependencies using Poetry.
	poetry install

.PHONY: poetry-rm-env
poetry-rm-env: ## Removes Poetry virtual environment and lock file.
	poetry env remove --all && rm poetry.lock

.PHONY: poetry-shell
poetry-shell: ## Launch a shell within Poetry virtual environment.
	poetry shell

.PHONY: poetry-to-requirements
poetry-to-requirements: ## Export poetry requirements to requirements.txt
	poetry export -f requirements.txt --output setup/requirements.txt --without-hashes

.PHONY: ruff-format
ruff-format: ## Format codebase using Ruff
	ruff check --select I --fix .
	ruff format .

.PHONY: ruff-lint
ruff-lint: ## Lint codebase using Ruff
	ruff check . --fix

.PHONY: run-mkdocs
run-mkdocs: ## Run the MkDocs server
	cd docs && mkdocs serve

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
help: ## Display this help
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "; printf "\033[1m%-20s %-50s\033[0m\n", "Target", "Description"; \
	              printf "%-20s %-50s\n", "------", "-----------";} \
	      /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %-50s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
