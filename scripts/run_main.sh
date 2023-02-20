#!/bin/bash
set +x

export OPENAI_API_KEY=""

make clean
python src/main.py
bash scripts/build_md.sh