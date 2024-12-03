SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

# Directories
target := hyperweave
DOCS_PATH := docs
SCRIPTS_PATH := scripts

# GitHub Actions
ACT := act
ACT_ENV_FILE := .env
ACT_WORKFLOW_DIR := .github/workflows/ci.yml

# Commands
UV := uv
UV_TOOL := $(UV) tool
MYPY_CMD := $(UV) mypy
NOX_CMD := $(UV) run nox
PYTEST_CMD := $(UV) run pytest
RUFF_CMD := $(UV) run ruff


# -- Cleanup -----------------------------------------------------------------------------------------


.PHONY: all
all: clean install format lint test  ## Clean, install, format, lint, and run tests


.PHONY: clean
clean: ## Remove project build artifacts
	@$(SCRIPTS_PATH)/clean.sh clean-pyc


# -- Documentation ---------------------------------------------------------------------------------


.PHONY: docs
docs: ## Serve Mkdocs site locally
	cd $(DOCS_PATH) && $(UV) run mkdocs serve


# -- Code Quality ----------------------------------------------------------------------------------

.PHONY: format-toml
format-toml: ## Format TOML files using tomlfmt
	$(UV) run pyproject-fmt pyproject.toml --indent 4

.PHONY: format
format: ## Format codebase using Ruff
	$(RUFF_CMD) format $(target)

.PHONY: lint
lint: ## Lint codebase using Ruff
	$(RUFF_CMD) check $(target) --fix

.PHONY: type-check
type-check: ## Type-check codebase using mypy
	$(UV) run mypy $(target)


# -- Testing ---------------------------------------------------------------------------------------


.PHONY: test-ci
test-ci: ## Test GitHub Actions workflows locally
	$(ACT) -W $(ACT_WORKFLOW_DIR) --container-architecture linux/amd64

.PHONY: test
test: ## Run unit tests using Pytest
	$(PYTEST_CMD)

.PHONY: test-nox
test-nox: ## Run tests across all environments
	$(NOX_CMD) -f noxfile.py


# -- uv --------------------------------------------------------------------------------------------


.PHONY: uv-install
uv-install: ## Install all project dependencies
	$(UV) pip install -r pyproject.toml --all-extras

.PHONY: uv-lock
uv-lock: ## Lock dependencies declared in pyproject.toml
	$(UV) pip compile pyproject.toml --all-extras

.PHONY: uv-sync
uv-sync: ## Sync environment with pyproject.toml
	$(UV) pip sync pyproject.toml

.PHONY: uv-venv
uv-venv: ## Create a virtual environment using uv
	$(UV) venv --python 3.11


# -- Utilities -------------------------------------------------------------------------------------


.PHONY: search
search: ## Search for items in the codebase
	grep -Ril ${WORD} .


.PHONY: help
help: Makefile ## Display the help menu
	@echo -e ""
	@echo -e "Usage: make [target]"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo -e "__________________________________________________________________________________________\n"
