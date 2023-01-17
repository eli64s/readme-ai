"""src/format.py
"""
import pandas as pd


def create_html():
    result = """
    <html><body>
    <div>
        <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
            width="80"><h1>OpenAI Auto Markdown Docs</h1>
        <hr>
        <h3>Software and Packeges</h3>
            <p>[description]</p>
            <p><img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />
            <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" />
            </p>
    </div>
    <hr>
    <div>
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg"
        width="80" />
    <h2>Repository Structure</h2>
    <h3>Modules (src)</3<div></div>"""

    data = pd.read_csv("data/output/docs.csv")
    for i, j in data.iterrows():
        script = j[0].split("/")[1]
        tag = f"""
        <div>
            <dl>
                <dt>{script}</dt>
                <dd>{j[1]}</dd>
            </dl>
        </div>"""
        result = f"{result}{tag}"
    result = f"""{result}
    <hr>
    <div>
        <h3>Roadmap</h3>
        <p>[description]</p>
    </div>
    <hr></body></html>"""
    return result
