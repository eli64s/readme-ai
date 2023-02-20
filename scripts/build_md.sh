#!/bin/bash

pandoc --to=markdown_strict -o docs/markdown/_readme.md docs/html/readme.html
perl -pi -w -e 's/style="width: 80%;"/width="80"/g;' docs/markdown/_readme.md

tree --dirsfirst --noreport -I docs/markdown/tree.md |
sed '1s/^/```bash\n/;$s/$/\n```/' > docs/markdown/tree.md

cat docs/markdown/_readme.md docs/markdown/tree.md | pandoc -f markdown -t markdown -o docs/markdown/temp_1.md

sed 's/^\`*<img/<img/' docs/markdown/temp_1.md > docs/markdown/temp_2.md
sed 's/width="80" \/>`{=html}/width="80" \/>/g' docs/markdown/temp_2.md > docs/markdown/temp_3.md

pandoc --to=markdown_strict -o docs/markdown/setup.md docs/html/setup.html
cat docs/markdown/temp_3.md docs/markdown/setup.md | pandoc -f markdown -t markdown -o docs/markdown/temp_4.md

sed 's/^\`*<img/<img/' docs/markdown/temp_4.md > docs/markdown/temp_5.md
sed 's/width="80" \/>`{=html}/width="80" \/>/g' docs/markdown/temp_5.md > docs/markdown/readme.md

sed -i -e '/## Usage readme.md' -e '//d' path/to/target_file.md
