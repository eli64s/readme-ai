#!/bin/bash
set +x

#export OPENAI_API_KEY=""

python -m spacy download en_core_web_sm

python src/main.py