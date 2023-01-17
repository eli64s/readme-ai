"""src/format.py
"""
import pandas as pd

md_title = """
<a style="vertical-align:middle">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100"; style="vertical-align:middle" />
<span style="vertical-align:middle">
<h1>OpenAI Auto Markdown Docs</h1>
</span></a>
"""

repo_title = """
<a style="vertical-align:middle">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="100"; style="vertical-align:middle" />
<span style="vertical-align:middle">
<h2>Repository</h2>
</span></a>
"""


def create_html():
    data = pd.read_csv(
        "/Users/k01101011/Documents/GitHub/gpt3_markdown_automation/data/output/docs.csv"
    )
    build_str = """\
    <a style="vertical-align: middle"><img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg"
    width="100"; style="vertical-align: middle" /><span style="vertical-align: middle"><h2>Modules (src)</h2>
    </span></a>"""
    for i, j in data.iterrows():
        build_str += f"""<div><h4><a id="{j[0]}"></a><h4>{j[0]}</h4><p>{j[1]}</p> </div>"""

    html_str = f"{md_title}<br>{repo_title}<br>{build_str}"

    return html_str
