
<div align="center">
<h1 align="center">

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">

<div><p>PydocsAI</p></h1>

<h3 align="center">[insert-project-summary]</h3>

![openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)![sh](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

</div>


---

## Overview

> [insert-description]

## Feautres

> [insert-description]

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## Repository Structure
```bash
/var/folders/k8/9bv99nsj41g6f9_b63qh1__80000gn/T/tmpl4du7sp3
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   └── conf.toml
├── docs
│   ├── imgs
│   │   ├── docs.png
│   │   ├── head.png
│   │   └── tree.png
│   ├── raw_data.csv
│   └── readme.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── auto_docstrings.sh
│   └── run_main.sh
├── setup.py
├── src
│   ├── __init__.py
│   ├── builder.py
│   ├── conf.py
│   ├── logger.py
│   ├── main.py
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

7 directories, 30 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## Modules
## src
| file         | summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conf.py      | This code defines a class called AppConfig which contains five other classes: OpenAI, GitHub, Markdown, Paths, and AppConfig. Each of these classes contains variables that are used to store information related to the project.                                                                                                                                                                                                                                        |
| processor.py | This code provides functions to clone a GitHub repository, parse the codebase, and get packages and extensions from the codebase. It uses the git library to clone the repository to a temporary directory, and then uses the pipreqs library to get the packages from the codebase. It also uses the os and shutil libraries to walk through the directory and get the file extensions. Finally, it uses the pathlib library to get each file as a raw string.          |
| logger.py    | This code creates a Logger class that is used to log messages with different levels of severity. It imports the logging and colorlog modules and configures the logger with a StreamHandler and a ColoredFormatter. It also provides methods for logging messages with different levels of severity.                                                                                                                                                                     |
| model.py     | This code imports the OpenAI library and sets the API key from the environment. It then defines a function, code_to_text(), which takes an engine and a dictionary of files and code as parameters. The function iterates through the files and code, skips any files that are not Python files, and creates a prompt for each file. It then uses the OpenAI library to generate a summary of the code and appends the file and summary to a list. Finally, the function |
| builder.py   | This code is a function that builds a markdown file from a configuration file, a list of packages, and a URL. It uses the FileFactory class to read and write files, the pandas library to read a CSV file, and the git library to clone a repository. It also uses the subprocess library to run the tree command. The function gets badges from a JSON file, creates a header with the badges, creates tables from a CSV file, and creates a tree from the cl          |
| utils.py     | The provided Python code is a FileFactory class that is used to read and write different types of files. It imports the csv, json, and toml modules and has methods for reading and writing files of different types, such as CSV, JSON, HTML, MD, and TOML.                                                                                                                                                                                                             |
| main.py      | """                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|              | This code is for a program called PydocsAI. It reads a configuration file, clones a codebase from a given URL, and uses an OpenAI engine to generate a code summary. It then writes the code summary to a CSV file and builds the project readme docs. Finally, it logs the completion of the program.                                                                                                                                                                   |
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


## Roadmap


- [x]

- []

- []


## Contribute


> [insert-description]


## Acknowledgments


> [insert-description]


---
