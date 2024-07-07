COMMITS := 10
SHELL := /bin/bash
VENV := readmeai
VV := \

.PHONY: clean
clean: ## Remove project build artifacts
	@echo -e "\nFile clean up in directory: ${CURDIR}"
	./scripts/clean.sh clean

.PHONY: format
format: ## Format codebase using Ruff
	@echo -e "\nFormatting in directory: ${CURDIR}"
	ruff check --select I --fix .
	ruff format .

.PHONY: lint
lint: ## Lint codebase using Ruff
	@echo -e "\nLinting in directory: ${CURDIR}"
	ruff check . --fix

.PHONY: conda-recipe
conda-recipe: ## Create conda recipe for conda-forge
	grayskull pypi readmeai
	conda build .

.PHONY: git-rm-cache
git-rm-cache: ## Remove all files from git cache
	git rm -r --cached .

.PHONY: git-log
git-log: ## Display git log for last ${COMMITS} commits
	git log -n ${COMMITS} --pretty=tformat: --shortstat

.PHONY: nox
nox: ## Run nox test automation against multiple Python versions
	nox -f noxfile.py

.PHONY: pytest
pytest: ## Run unit tests using pytest
	poetry run pytest ${VV}

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
poetry-to-requirements: ## Export poetry requirements to requirements.txt
	poetry export -f requirements.txt --output setup/requirements.txt --without-hashes

.PHONY: search
search: ## Search for a word in the codebase
	@echo -e "\nSearching for: ${WORD} in directory: ${CURDIR}"
	grep -Ril ${WORD} readmeai tests scripts setup

.PHONY: help
help: Makefile ## Display this help message
	@echo -e ""
	@echo -e "Usage: make [target]"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo -e "__________________________________________________________________________________________\n"
