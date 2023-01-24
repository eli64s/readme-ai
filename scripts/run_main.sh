#!/bin/bash
set +x

#export API_SK=

python src/main.py

pandoc --to=markdown_strict -o docs/output.md docs/html_docs.html
#perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' docs/output.md

make clean

tree --dirsfirst --noreport -I docs/tree.md |
sed '1s/^/```bash\n/;$s/$/\n```/' > docs/tree.md