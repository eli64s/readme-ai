SHELL = /bin/bash
VENV := readmeai

.PHONY: help style clean conda venv mem_profile profile

# Help
help:
	@echo "Commands:"
	@echo "clean      : cleans all unnecessary files."
	@echo "style      : executes style formatting."
	@echo "conda      : creates a conda environment."
	@echo "venv       : creates a virtual environment."
	@echo "profile    : runs cProfile on the CLI script."
	@echo "snakeviz   : runs SnakeViz on the profile.out file."

# Style
.PHONY: style
style:
	-black .
	-flake8
	-isort .

# Clean
.PHONY: clean
clean: style
	bash scripts/clean.sh

# Conda Environment
conda:
	conda create -n $(VENV) python=3.9 -y
	conda activate $(VENV) && pip install -r requirements.txt

# Python Virtual Environment
venv:
	python -m venv $(VENV)
	source venv/bin/activate
	pip install -r requirements.txt

# cProfile
profile:
	@echo "Running cProfile on CLI script"
	python -m cProfile -o profile.out -s cumulative src/main.py --output docs/README_001.md --remote https://github.com/eli64s/README-AI

# SnakeViz
snakeviz:
	@echo "Running SnakeViz on profile.out file"
	snakeviz profile.out
