<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
width="80" />

# PydocsAI

\[insert-project-summary\]

#### Software & Packages

![](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

------------------------------------------------------------------------

### Overview

\[insert-description\]

------------------------------------------------------------------------

### Use-Case

\[insert-description\]

------------------------------------------------------------------------

### Features

\[insert-description\]

------------------------------------------------------------------------

<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg"
width="80" />

### Modules

SRC

#### processor.py

This code provides functions to clone a GitHub repository, get the
packages and file extensions used in the repository, and parse the
codebase into a dictionary. It also provides a context manager to clone
the repository to a temporary directory.

#### logger.py

This code creates a Logger class that is used to log messages with
different levels of severity. It imports the logging and colorlog
modules and configures the logger with a StreamHandler and a
ColoredFormatter. It also provides methods for logging messages with
different levels of severity.

#### model.py

This code imports the OpenAI library and sets the API key from the
environment. It then defines a function, code_to_text(), which takes an
engine and a dictionary of files and code as parameters. The function
iterates through the files and code, skips any files that are not Python
files, and creates a prompt for each file. It then uses the OpenAI
library to generate a summary of the code and appends the file and
summary to a list. Finally, the function

#### builder.py

This code is used to build a HTML page from a given configuration file,
a list of packages, and a URL. It reads a JSON file containing badges,
creates a header with the badges, creates a body from a CSV file, and
creates a setup page. It also clones a repository from the given URL and
creates a tree.md file with the directory structure of the repository.

#### utils.py

The FileFactory class is a Python module that provides methods for
reading and writing various file types, such as JSON, CSV, HTML,
Markdown, and TOML. It takes a base path as an argument and uses it to
construct the file path for the specified file name.

#### main.py

This code is a Python script that reads a configuration file, clones a
codebase from a given URL, uses an OpenAI engine to generate a code
summary, writes the summary to a CSV file, and builds a project readme.

------------------------------------------------------------------------

<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg"
width="80" />

### Repository Structure

``` bash
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   └── conf.toml
├── docs
│   └── gpt
│       ├── body.png
│       └── head.png
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
│   ├── model.py
│   ├── processor.py
│   └── utils.py
├── tests
│   ├── conftest.py
│   ├── test_builder.py
│   ├── test_conf.py
│   ├── test_logger.py
│   ├── test_main.py
│   ├── test_model.py
│   ├── test_processor.py
│   └── test_utils.py
└── tree.md
```

------------------------------------------------------------------------

## Getting Started

\[insert-description\]

### Usage

    # 1. Clone GitHub repository.
    git clone https://github.com/eli64s/PydocsAI && cd PydocsAI

## Contribute

-   Contributions and suggestions welcome!

------------------------------------------------------------------------
