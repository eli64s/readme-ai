"""src/format.py
"""
import pandas as pd


def create_html():
    closing_tags = """
        </div>
            <hr>
            <div>
                <h3>Roadmap</h3>
                <p>[description]</p>
            </div>
            <hr>
            <div>
                <h3>Licenses</h3>
                <p>[description]</p>
            </div>
            <hr>
        </body>
        </html>
    """

    result = """
    <html>

    <body>
        <div>
            <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
                width="80">
            <h1>OpenAI Auto Markdown Docs</h1>
            <hr>
            <h3>Software and Packeges</h3>
            <p>[description]</p>
            <p>
                <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />
                <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" />
                <img src="https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white" />
                <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" />
                <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" />
                <img src="https://img.shields.io/badge/pre-commit-FAB040?style=for-the-badge&logo=precommit&logoColor=FAB040" />
            </p>
            <p>
                <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" />
                <img src="https://img.shields.io/badge/CondaForge-000000.svg?style=for-the-badge&logo=Conda-Forge&logoColor=white" />
                <img src="https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E" />
                <img src="https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white" />
                <img src="https://img.shields.io/badge/Shields.io-000000.svg?style=for-the-badge&logo=shieldsdotio&logoColor=white" />
            </p>
        </div>
        <hr>
        <div>
            <h3>Overview</h3>
            <p>[description]</p>
            <hr>
            <h3>Prerequistes</h3>
            <p>[description]</p>
        </div>
        <hr>
        <div>
            <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg"
            width="80" />
            <h3>Repository Structure</h3>
            <p>[description]</p>
        </div>
        <hr>
        <div>
            <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" 
            width="80" />
            <h3>Modules [src]</h3>
    """

    data = pd.read_csv("output/data/docs.csv")

    for i, j in data.iterrows():
        script = j[0].split("/")[1]
        tag = f"""
        <dl>
            <dt><b><i>{script}</i></b></dt>
            <dd>{j[1]}</dd>
        </dl>
        """
        result = f"{result}{tag}"
    return f"{result}{closing_tags}"
