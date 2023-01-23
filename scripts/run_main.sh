#!/bin/bash
set +x

#export API_SK=

python src/main.py

pandoc --to=markdown_strict -o output/output.md output/html_docs.html
perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' output/output.md

make clean

tree --dirsfirst --noreport -I output/tree.md |
sed '1s/^/```bash\n/;$s/$/\n```/' > output/tree.md