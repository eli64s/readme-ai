SHELL := /bin/bash
TARGET := readmeai
TARGET_TEST := tests
PYPROJECT_TOML := pyproject.toml

# -- Development --------------------------------------------------------------


.PHONY: clean
clean: ## Clean project files
	./scripts/clean.sh clean-pyc


# -- Documentation ----------------------------------------------------------------------


.PHONY: docs
docs: ## Build and serve Mkdocs documentation
	cd docs && mkdocs build && mkdocs serve


# -- Docker --------------------------------------------------------------------


.PHONY: docker-build
docker-build: ## Build Docker image for application
	docker build -t zeroxeli/readme-ai:latest .


# -- Poetry --------------------------------------------------------------------


.PHONY: install
install: ## Install project dependencies using Poetry
	poetry install

.PHONY: rm-environment
rm-environment: ## Remove Poetry virtual environment.
	poetry env remove --all && rm poetry.lock

.PHONY: shell
shell: ## Start a shell within the Poetry virtual environment
	poetry shell

.PHONY: to-requirements
to-requirements: ## Export Poetry dependencies to requirements.txt
	poetry export -f requirements.txt --output setup/requirements.txt --without-hashes


# -- Code Quality --------------------------------------------------------------


.PHONY: format
format: ## Format codebase using Ruff
	poetry run ruff format $(TARGET)

.PHONY: lint
lint: ## Lint codebase using Ruff
	poetry run ruff check $(TARGET) --fix


# -- Testing -------------------------------------------------------------------


.PHONY: test
test: ## Run test suite using Pytest
	poetry run pytest $(TARGET_TEST) --config-file $(PYPROJECT_TOML)

.PHONY: test-nox
test-nox: ## Run test suite using Nox
	nox -f noxfile.py


# -- Utilities ----------------------------------------------------------------


.PHONY: search
search: ## Search for a word across project files
	grep -Ril ${WORD} $(TARGET) docs tests

.PHONY: help
help: ## Display this help
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "; printf "\033[1m%-20s %-50s\033[0m\n", "Target", "Description"; \
	              printf "%-20s %-50s\n", "------", "-----------";} \
	      /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %-50s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
