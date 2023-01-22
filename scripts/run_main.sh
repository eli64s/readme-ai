#!/bin/bash
set +x

API_SK="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"
export API_SK

python src/main.py

rm -rf _tmp
rm -rf outputs