
<div align="center">
<h1 align="center">

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">

<div><p>PydocsAI</p></h1>

<h3 align="center">[insert-project-summary]</h3>

![openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)![html](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)

![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)![sh](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

</div>


---

## Overview

> [insert-description]

## Use-Case

> [insert-description]

## Feautres

> [insert-description]

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## Repository Structure
```bash
/var/folders/k8/9bv99nsj41g6f9_b63qh1__80000gn/T/tmpbal_q9h4
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   └── conf.toml
├── docs
│   ├── gpt
│   │   ├── body.png
│   │   ├── head.png
│   │   ├── raw_data.csv
│   │   └── tree.png
│   ├── html
│   │   └── readme.html
│   └── markdown
│       └── readme.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── auto_docstrings.sh
│   ├── build_md.sh
│   └── run_main.sh
├── setup.py
├── src
│   ├── __init__.py
│   ├── builder.py
│   ├── conf.py
│   ├── logger.py
│   ├── main.py
│   ├── md_helper.py
│   ├── model.py
│   ├── processor.py
│   └── utils.py
└── tests
    ├── conftest.py
    ├── test_builder.py
    ├── test_conf.py
    ├── test_logger.py
    ├── test_main.py
    ├── test_model.py
    ├── test_processor.py
    └── test_utils.py

9 directories, 33 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## Modules
## src
| file         | summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conf.py      | This code defines a class called AppConfig which contains five other classes: OpenAI, GitHub, Html, Paths, and AppConfig. Each of these classes contains variables that are used to store information related to the project. The OpenAI class stores engine and key information, the GitHub class stores a URL, the Html class stores head, body, setup, and tree information, and the Paths class stores badge, docs, html, and md file paths.                         |
| processor.py | This code provides functions to clone a GitHub repository, get the packages and file extensions used in the repository, and parse the codebase into a dictionary. It also provides a context manager to clone the repository to a temporary directory.                                                                                                                                                                                                                   |
| logger.py    | This code creates a Logger class that is used to log messages with different levels of severity. It imports the logging and colorlog modules and configures the logger with a StreamHandler and a ColoredFormatter. It also provides methods for logging messages with different levels of severity.                                                                                                                                                                     |
| model.py     | This code imports the OpenAI library and sets the API key from the environment. It then defines a function, code_to_text(), which takes an engine and a dictionary of files and code as parameters. The function iterates through the files and code, skips any files that are not Python files, and creates a prompt for each file. It then uses the OpenAI library to generate a summary of the code and appends the file and summary to a list. Finally, the function |
| builder.py   | This code builds an HTML page with a header, body, and tree. It reads a JSON file containing badges, and uses the badges to create a header for the HTML page. It also reads a CSV file to create tables in Markdown format, and uses a git repository URL to generate a tree in Markdown format. Finally, it writes the HTML, Markdown, and setup files to the appropriate directories.                                                                                 |
| md_helper.py | This Python code reads the content of two Markdown files, one containing the main content and one containing the new content to be inserted. It then finds the index of the header after which the new content should be inserted and inserts it. Finally, it combines the sections into a single Markdown string and writes the updated content to the main file.                                                                                                       |
| utils.py     | FileFactory is a class that provides methods to read and write data from/to different file formats (JSON, CSV, HTML, Markdown, and TOML). It takes a base path as an argument and uses it to construct the file path for the file to be read/written.                                                                                                                                                                                                                    |
| main.py      | This code is a Python script that reads a configuration file, clones a codebase from a given URL, uses an OpenAI engine to generate a code summary, writes the summary to a CSV file, and builds a project readme.                                                                                                                                                                                                                                                       |
---

## Getting Started


### Usage

```Bash
# 1. Clone GitHub repository.
git clone https://github.com/eli64s/PydocsAI && cd PydocsAI


# 2...


# 3...

```


---


## Contribute


> [insert-description]


## Roadmap


> [insert-description]


## References


> [insert-description]


---
