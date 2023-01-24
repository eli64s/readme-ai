#!/bin/bash
set +x

#export API_SK=

python src/main.py

pandoc --to=markdown_strict -o docs/output.md docs/html_docs.html
perl -pi -w -e 's/# </</g;' docs/output.md

make clean

tree --dirsfirst --noreport -I docs/tree.md |
