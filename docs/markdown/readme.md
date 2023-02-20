<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
width="80" />

# PyDocsAI

\[insert-project-summary\]

#### Software & Packages

![](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
![](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)

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

##### processor.py

This code provides functions to clone a GitHub repository to a temporary
directory, get file extensions and packages from the repository, and
parse the repository into a dictionary of file contents.

##### logger.py

This code sets up a logger with a ColoredFormatter, which will display
log messages in different colors depending on the log level. It also
sets the log level to DEBUG.

##### model.py

This code uses the OpenAI API to summarize the code in a Python script.
It takes in an engine and a dictionary of files and code as parameters.
It then creates a prompt with the code and uses the OpenAI API to
generate a summary of the code. The summary is then added to a list of
documents and returned.

##### builder.py

This Python code is a function that creates an HTML page with a header
and body. It takes in a configuration file, a list of badges, a name,
and a path as parameters. It uses the pandas library to read a CSV file
and iterates through the rows to create a summary and description for
each file. It also uses a function called get_icons to map the names of
packages to their corresponding badges.

##### utils.py

This Python code defines a FileHandler class that can be used to read
and write files in different formats. It has three methods: read_json(),
write_html(), and write_md(). The read_json() method reads a JSON file
and returns its contents. The write_html() and write_md() methods write
HTML and Markdown files, respectively. The class takes an object as an
argument and sets the paths for the JSON, HTML, and Markdown files.

##### main.py

This code imports several modules and sets up a logger. It then loads a
configuration file, clones a codebase, and creates a list of project
dependencies. It then creates a header and HTML documentation, and
writes the HTML to a file. Finally, it logs that the markdown
documentation is complete.

------------------------------------------------------------------------

<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg"
width="80" />

### Repository Structure

``` bash
.
├── conf
│   ├── badges.json
│   └── conf.toml
├── docs
│   ├── gpt
│   │   ├── body.png
│   │   ├── head.png
│   │   └── raw_data.csv
│   ├── html
│   │   ├── readme.html
│   │   └── setup.html
│   └── markdown
│       ├── _readme.md
│       └── tree.md
├── notebooks
│   ├── data_validation.ipynb
│   └── markdown.py
├── scripts
│   ├── auto_docstrings.sh
│   ├── build_all.sh
│   ├── build_md.sh
│   └── run_main.sh
├── src
│   ├── __pycache__
│   │   ├── builder.cpython-39.pyc
│   │   ├── conf.cpython-39.pyc
│   │   ├── logger.cpython-39.pyc
│   │   ├── model.cpython-39.pyc
│   │   ├── processor.cpython-39.pyc
│   │   └── utils.cpython-39.pyc
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
├── Makefile
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py
```

------------------------------------------------------------------------

## Getting Started

\[insert-description\]

### Usage

    # 1. Clone GitHub repository.
    git clone https://github.com/eli64s/PyDocsAI && cd PyDocsAI

## Contribute

-   Contributions and suggestions welcome!

------------------------------------------------------------------------
