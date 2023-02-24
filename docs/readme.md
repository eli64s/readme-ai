
<div align="center">
<h1 align="center">

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">

<div><p>PydocsAI</p></h1>

  <h3 align="center">[insert-project-summary]</h3>

![openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)![sh](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

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
.
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
│   ├── run_main.sh
│   └── test.sh
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
| file         | summary                                                                                                                                                                                                                                                                                                                                                       |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conf.py      | This code defines a class called AppConfig which contains five other classes: OpenAI, GitHub, Markdown, Paths, and AppConfig. Each of these classes contains variables that are used to store information related to the project.                                                                                                                             |
| processor.py | This code is a function that clones a GitHub repository to a temporary directory, parses the codebase, and returns a map of all repo contents. It also gets the file extensions and packages used in the codebase to help generate project badge icons.                                                                                                       |
| logger.py    | This Python code creates a Logger class that is used to log messages with different levels of severity. It imports the logging and colorlog modules and sets up a StreamHandler to format the log messages with colors. It also provides methods for logging messages with different levels of severity.                                                      |
| model.py     | This code is a Python class that uses the OpenAI Codex API to summarize Python code. It takes in a dictionary of file names and code contents, and returns a dictionary of file names and code summaries. It also includes an exception class for when an error occurs with the OpenAI API.                                                                   |
| builder.py   | This code is a function that builds a markdown file from a configuration object, a list of packages, and a URL. It reads a CSV file, reads a JSON file, and uses the git library to clone a repository. It then formats the markdown file with the data from the CSV and JSON files, and the repository tree. Finally, it writes the markdown file to a file. |
| utils.py     | The provided Python code is a FileFactory class that is used to read and write different types of files. It imports the csv, json, and toml modules and has methods for reading and writing files of different types, such as CSV, JSON, HTML, MD, and TOML.                                                                                                  |
| main.py  | This code is for a program called PydocsAI. It reads a configuration file, clones a codebase from a given URL, and uses an OpenAI engine to generate a code summary. It then writes the summary to a CSV file and builds the project readme docs. Finally, it logs the completion of the process.                                                             |
---


## Getting Started


### Prerequisites


Before you begin, ensure that you have the following prerequisites installed:


> - [insert-prerequisites-if-needed]


### Installation


1. Clone the PydocsAI repository:


```sh
git clone https://github.com/eli64s/PydocsAI && cd PydocsAI
```


2. Create a new Conda environment and install the required dependencies:


```sh
conda env create -f setup/environment.yaml
conda activate PydocsAI
```


> 3. [insert-additional-steps]


```sh
 #... 
```


### Running PydocsAI


```sh
# ... 
```


---


## Roadmap


> - [X] [insert-task]

> - [ ] [insert-task]

> - [ ] [insert-task]


---


## Contributing

> [insert-description]

---

## 🙏 Acknowledgments

> [insert-description]

---
