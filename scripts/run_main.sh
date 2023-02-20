#!/bin/bash
set +x

export OPENAI_API_KEY=""

make clean

python src/main.py

find docs/markdown -type f ! -name 'readme.md' -delete
find docs/html -type f ! -name 'readme.html' -delete