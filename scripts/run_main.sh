#!/bin/bash
set +x

API_SK=""
export API_SK

python src/main.py

rm -rf _tmp
rm -rf outputs