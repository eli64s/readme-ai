#!/bin/bash

pandoc --to=markdown_strict -o docs/markdown/_readme.md docs/html/readme.html
perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' docs/markdown/_readme.md

tree --dirsfirst --noreport -I docs/markdown/tree.md |
sed '1s/^/```bash\n/;$s/$/\n```/' > docs/markdown/tree.md

pandoc --to=markdown_strict -o docs/markdown/setup.md docs/html/setup.html
cat docs/markdown/tree.md docs/markdown/setup.md | pandoc -f markdown -t markdown -o docs/markdown/_readme_.md

cat docs/markdown/_readme.md docs/markdown/_readme_.md | pandoc -f markdown -t markdown -o docs/markdown/readme_temp.md

sed 's/^\`*<img/<img/' docs/markdown/readme_temp.md > docs/markdown/readme.md
sed 's/width="80" \/>`{=html}/width="80" \/>/g' docs/markdown/readme.md > docs/markdown/readme2.md

find docs/markdown -type f ! -name 'readme.md' -delete
find docs/markdown -type f ! -name 'readme.html' -delete