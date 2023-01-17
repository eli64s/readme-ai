<a style="vertical-align:middle">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100"; style="vertical-align:middle" />
<span style="vertical-align:middle">
<h1>OpenAI Auto Markdown Docs</h1></span></a>

### *NOT COMPLETED: Work In Progress !*

This project generates a clean and structured Markdown template to kickstart your machine learning projects.  
Leverages OpenAI API models to convert Python code to natural language, providing boilerplate summaries for our codebase.

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-13ADC7.svg?style=for-the-badge&logo=DVC&logoColor=white)
![pre-commit](https://img.shields.io/badge/pre-commit-FAB040?style=for-the-badge&logo=precommit&logoColor=FAB040)
![prettier](https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E)
![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

---

## Overview

OpenAI API is leveraged to generate boilerplate codebase documentation in a structured and clean format. Developers can focus on the more critical aspects of their project documentation and refine OpenAI's boilerplate summaries.

- Generates README Markdown documentation for all Python files in your repository.
- Analyzes project dependencies to structure and style markdown header with [Shields.io](https://shields.io/) badges.

## Prerequisites
### 🤖 OpenAI API
- [OpenAI API](https://beta.openai.com/docs/introduction)
### 🛡 Shields.io (optional)
- [Shields.io](https://shields.io/)
### Automate Docstrings (optional)
- [Autodocstrings: Repository](https://github.com/cdesarmeaux/autodocstrings)
  
---
## Usage

```Bash
# 1. Clone GitHub repository.
git clone https://github.com/king-technologies/Project-Initiator.git && cd gpt_auto_markdown_docs

# 2. Setup conda virtual environment.
make conda

# 3. Run the model.
bash scripts/run_model.sh
```

<a style="vertical-align:middle">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="100"; style="vertical-align:middle" />
<span style="vertical-align:middle">
<h2>Repository</h2></span></a>

```shell
.
├── Makefile
├── README.md
├── configs
│   ├── __init__.py
│   ├── api
│   │   └── gpt.yaml
│   ├── config.yaml
│   ├── input
│   │   ├── github.yaml
│   │   └── local.yaml
│   └── logger
│       └── logger.yaml
├── data
│   └── output
│       └── docs.csv
├── notebooks
│   └── data_checks.ipynb
├── pyproject.toml
├── requirements.txt
├── setup
│   └── setup.sh
├── setup.py
└── src
    ├── __init__.py
    ├── logger.py
    ├── main.py
    ├── model.py
    └── processor.py
```

<a style="vertical-align:middle">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="100"; style="vertical-align:middle" />
<span style="vertical-align:middle">
<h2>Modules (src)</h2></span></a>

#### main.py

#### model.pu

#### processor.py

---

## Roadmap

- [ ] 
- [ ]

> <svg width="50" height="50" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0)"><path d="M0.000590812 131.108V42.8655C-0.00675869 42.5314 0.0545285 42.1993 0.180663 41.8898C0.306798 41.5803 0.495099 41.2999 0.733924 41.066C0.946982 40.8366 1.20476 40.6532 1.4914 40.5271C1.77803 40.401 2.08745 40.3349 2.40059 40.3329H34.9339C47.8228 40.3329 58.845 44.8872 68.0006 53.9958C77.1561 63.1044 81.7339 74.0569 81.7339 86.8534C81.7339 99.7387 77.1561 110.758 68.0006 119.911C58.845 129.064 47.8228 133.64 34.9339 133.64H2.40059C2.08745 133.638 1.77803 133.572 1.4914 133.446C1.20476 133.32 0.946982 133.137 0.733924 132.907C0.495099 132.673 0.306798 132.393 0.180663 132.084C0.0545285 131.774 -0.00675869 131.442 0.000590812 131.108V131.108ZM20.8006 113.913H33.6006C41.0673 113.913 47.2673 111.313 52.2006 106.115C57.1339 100.916 59.6006 94.4957 59.6006 86.8534C59.6006 79.2999 57.1339 72.9239 52.2006 67.7253C47.2673 62.5268 41.0673 59.9275 33.6006 59.9275H20.8006V113.913Z" fill="#13ADC7"/><path d="M95.1177 155.723L53.5177 66.0147C53.0732 65.126 53.0954 64.3262 53.5843 63.6153C54.0732 62.9044 54.8065 62.549 55.7843 62.549H73.5177C74.6732 62.549 75.4288 63.0377 75.7843 64.0152L97.7843 112.668H98.5843L120.584 64.0152C120.94 63.0377 121.695 62.549 122.851 62.549H140.584C141.562 62.549 142.295 62.9044 142.784 63.6153C143.273 64.3262 143.295 65.126 142.851 66.0147L100.984 155.723C100.451 156.701 99.6954 157.189 98.7176 157.189H97.3843C96.4065 157.189 95.651 156.701 95.1177 155.723V155.723Z" fill="#945DD6"/><path d="M128.865 121.111C119.532 111.78 114.865 100.45 114.865 87.12C114.865 73.7904 119.554 62.438 128.932 53.0628C138.31 43.6876 149.665 39 162.999 39C175.443 39 186.199 43.1322 195.265 51.3966C196.599 52.6407 196.643 53.8848 195.399 55.1289L184.999 65.9259C183.843 66.9923 182.732 66.9923 181.665 65.9259C176.599 61.3938 170.599 59.1278 163.665 59.1278C156.199 59.1278 149.976 61.8159 144.999 67.1922C140.021 72.5685 137.532 79.0334 137.532 86.5868C137.532 94.0514 140.043 100.427 145.065 105.715C150.087 111.002 156.332 113.646 163.799 113.646C170.732 113.646 176.687 111.513 181.665 107.248C182.91 106.181 184.065 106.226 185.132 107.381L195.532 118.445C196.687 119.6 196.643 120.8 195.399 122.044C186.51 130.664 175.71 134.973 162.999 134.973C149.665 134.973 138.287 130.353 128.865 121.111V121.111Z" fill="#F46737"/></g></svg>


---
## Licenses, Copyrights & Trademarks

- [References](https://github.com/simple-icons/simple-icons/blob/develop/DISCLAIMER.md#licenses-copyrights--trademarks)

---

<a style="vertical-align: middle">
    <img src=https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg
        width="100" ; style="vertical-align: middle" />
    <span style="vertical-align: middle">
        <h2>Modules (src)</h2>
    </span>
</a>


<div>
    <h4><a id="connectors/postgres.py"></a>
        <h4>connectors/postgres.py</h4>
        <p>This Python script creates a PostgreSQL database and two tables within it. It connects to the PostgreSQL
            database using psycopg2, drops the database if it already exists, creates the database, grants all
            privileges to the user, and then creates the two tables. It also has a function to get the table name from
            the SQL query.</p>
</div>

<div>
    <h4><a id="connectors/mysql.py"></a>
        <h4>connectors/mysql.py</h4>
        <p>def main():
            print("This program will calculate the average of two numbers")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            average = (num1 + num2) / 2
            print("The average of the two numbers is:", average)

            This code is a program that calculates the average of two numbers entered by the user. It prompts</p>
</div>

<div>
    <h4><a id="src/train.py"></a>
        <h4>src/train.py</h4>
        <p>This Python script loads parameters from a YAML file, loads a matrix from a pickle file, and uses the matrix
            to train a Random Forest Classifier. The classifier is then saved to an output file.</p>
</div>

<div>
    <h4><a id="src/evaluate.py"></a>
        <h4>src/evaluate.py</h4>
        <p>This Python script evaluates a model and its features using metrics such as average precision score, ROC AUC
            score, and precision-recall curve. It also creates plots for the ROC curve, confusion matrix, and feature
            importance. It takes two arguments, the model file and the features file, and uses the train and test files
            from the features file.</p>
</div>

<div>
    <h4><a id="src/prepare.py"></a>
        <h4>src/prepare.py</h4>
        <p>This Python script prepares data for a machine learning model. It reads in a data file, splits it into a
            training and test set, and writes the data to two output files. It also processes the data by removing extra
            whitespace and adding a label to each line based on the presence of a target tag.</p>
</div>

<div>
    <h4><a id="src/featurization.py"></a>
        <h4>src/featurization.py</h4>
        <p>This Python script reads in two data files (train.tsv and test.tsv) from a specified directory, uses the
            CountVectorizer and TfidfTransformer functions from the sklearn library to generate feature matrices, and
            saves the matrices in a specified directory as pickle files. It also prints out the size and data type of
            the output matrices.</p>
</div>

<div>
    <h4><a id="hydra/my_app.py"></a>
        <h4>hydra/my_app.py</h4>
        <p>"""
            This Python script uses the Hydra configuration manager to read a CSV file, get the full path of the input
            file, get the schema information from the configuration, and log the DataFrame and Config.</p>
</div>

<div>
    <h4><a id="hydra/my_app_dataclass.py"></a>
        <h4>hydra/my_app_dataclass.py</h4>
        <p>"""
            This Python script defines two classes, DBConnection and its subclasses MySQLConnection and
            PostgresConnection, which are used to connect to a database. It also defines three dataclasses, DBConfig,
            MySQLConfig, and PostgresConfig, which are used to store configuration information for the database
            connection. Finally, it defines a function, my_app, which uses the instantiate function to create a
            connection to the database.</p>
</div>