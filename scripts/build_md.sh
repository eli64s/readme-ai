#!/bin/bash
set +x

pandoc --to=markdown_strict -o docs/markdown/_readme.md docs/html/readme.html
perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' docs/markdown/_readme.md

cat docs/markdown/_readme.md docs/markdown/tree.md | pandoc -f markdown -t markdown -o docs/markdown/temp_1.md

sed 's/^\`*<img/<img/' docs/markdown/temp_1.md > docs/markdown/temp_2.md
sed 's/width="80" \/>`{=html}/width="80" \/>/g' docs/markdown/temp_2.md > docs/markdown/temp_3.md

pandoc --to=markdown_strict -o docs/markdown/setup.md docs/html/setup.html
cat docs/markdown/temp_3.md docs/markdown/setup.md | pandoc -f markdown -t markdown -o docs/markdown/temp_4.md

sed 's/^\`*<img/<img/' docs/markdown/temp_4.md > docs/markdown/temp_5.md
sed 's/width="80" \/>`{=html}/width="80" \/>/g' docs/markdown/temp_5.md > docs/markdown/readme.md

python src/md_helper.py

find docs/markdown -type f ! -name 'readme.md' -delete
find docs/html -type f ! -name 'readme.html' -delete