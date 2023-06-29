# Makefile

SHELL = /bin/bash
VENV := readmeai

.PHONY: help style clean conda venv profile snakeviz

# Help
help:
	@echo "Commands:"
	@echo "clean      : cleans all unnecessary files."
	@echo "style      : executes style formatting."
	@echo "conda      : create conda environment."
	@echo "venv       : creates python virtual environment."
	@echo "profile    : runs cProfile on the CLI script."
	@echo "snakeviz   : runs SnakeViz on the profile.out file."

# Style
.PHONY: style
style:
	-autoflake --remove-all-unused-imports --in-place --recursive .
	-autopep8 --in-place --recursive .
	-black .
	-flake8
	-isort .
	-yapf -i -r .

# Clean
.PHONY: clean
clean: style
	bash scripts/clean.sh

# Conda Environment
conda:
	conda create -n $(VENV) python=3.9 -y && \
	source $$(conda info --base)/etc/profile.d/conda.sh && \
	conda activate $(VENV) && \
	poetry install

# Python Virtual Environment
venv:
	poetry install

# cProfile
profile:
	@echo "Running cProfile on CLI script"
	python -m cProfile -o profile.out -s cumulative src/main.py --output docs/readme-ai.md --remote https://github.com/eli64s/readme-ai

# SnakeViz (pip install snakeviz)
snakeviz:
	@echo "Running SnakeViz on profile.out file"
	snakeviz profile.out
