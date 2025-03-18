SHELL := /bin/bash
PYPROJECT := pyproject.toml
TARGET := readmeai
TARGET_TEST := tests


# -------------
# Clean Up
# -------------

.PHONY: clean
clean: ## Clean project files
	./scripts/clean.sh clean-pyc


# -------------
# MkDocs Site
# -------------

.PHONY: docs
docs: ## Build and serve Mkdocs documentation
	cd docs && mkdocs build && mkdocs serve


# -------------
# Docker
# -------------

.PHONY: docker-build
docker-build: ## Build Docker image for application
	docker build -t zeroxeli/readme-ai:latest .


# -------------
# Environment
# -------------

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


# -------------
# Format & Lint
# -------------

.PHONY: format
format: ## Format codebase using Ruff
	poetry run ruff format $(TARGET)

.PHONY: lint
lint: ## Lint codebase using Ruff
	poetry run ruff check $(TARGET) --fix


# -------------
# Unit Tests
# -------------

.PHONY: test
test: ## Run test suite using Pytest
	@export PYTHONDONTWRITEBYTECODE=1 PYTHONPYCACHEPREFIX=/dev/shm && \
	poetry run pytest $(TARGET_TEST) --config-file=$(PYPROJECT)


.PHONY: test-nox
test-nox: ## Run test suite using Nox
	nox -f noxfile.py


# -------------
# TestPyPI
# -------------

VERSION_FILE := .version.tmp

.PHONY: testpypi-config
testpypi-config: ## Configure Poetry for TestPyPI
	@echo "Setting up TestPyPI repository..."
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	@echo "Don't forget to run: poetry config pypi-token.testpypi YOUR_TOKEN"

.PHONY: testpypi-build
testpypi-build: ## Build package for TestPyPI
	@echo "Building package for TestPyPI..."
	@# Generate a unique version with timestamp
	@poetry version 0.6.2a$$(date +%s)
	@# Store the version for later use
	@poetry version -s > $(VERSION_FILE)
	@poetry build

.PHONY: testpypi-publish
testpypi-publish: testpypi-build ## Publish package to TestPyPI
	@echo "Publishing to TestPyPI..."
	@poetry publish -r testpypi
	@echo "Published version $$(cat $(VERSION_FILE))"

.PHONY: testpypi-test
testpypi-test: ## Test package installation from TestPyPI
	@echo "Testing package installation from TestPyPI..."
	@if [ ! -f $(VERSION_FILE) ]; then \
		echo "Error: Version file not found. Run testpypi-publish first."; \
		exit 1; \
	fi
	pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ readmeai==$$(cat $(VERSION_FILE)) && \
	readmeai --help && \
	readmeai --version

.PHONY: testpypi-example
testpypi-example: ## Test package with example repository
	@echo "Testing package with example repository..."
	@if [ ! -f $(VERSION_FILE) ]; then \
		echo "Error: Version file not found. Run testpypi-publish first."; \
		exit 1; \
	fi
	pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ readmeai==$$(cat $(VERSION_FILE)) && \
	readmeai -r https://github.com/eli64s/readme-ai --api offline --output readme_testpypi.md
	# readmeai -r https://github.com/eli64s/markitecture --api openai --output readme_testpypi_markitect.md -hs modern -bs flat-square -t 0.9

.PHONY: testpypi
testpypi: testpypi-publish testpypi-test ## Full TestPyPI workflow (build, publish, test)
	@echo "TestPyPI workflow completed."

.PHONY: testpypi-cleanup
testpypi-cleanup: ## Clean up temporary version file
	@rm -f $(VERSION_FILE)
	@rm readme_testpypi.md readme_testpypi_markitect.md
	@echo "Cleanup completed."


# -------------
# Utilities
# -------------

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
