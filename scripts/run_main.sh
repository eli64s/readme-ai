#!/bin/bash
set +x

#export API_SK=

python src/main.py

rm -rf _tmp
rm -rf outputs

pandoc --to=markdown_strict -o output/output.md output/html_docs.html
perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' output/output.md
tree > output/tree.md