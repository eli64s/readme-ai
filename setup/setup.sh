#!/bin/bash

conda env create -f setup/env.yaml

eval "$(conda shell.bash hook)"
conda activate pydocsai

export PYTHONPATH=${PYTHONPATH}:${pwd}/src