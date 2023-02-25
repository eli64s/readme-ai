
<div align="center">
<h1 align="center">

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100">

<div><p>README-AI</p></h1>


> [insert-project-summary]

![openai](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)![py](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)![sh](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)![json](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)![markdown](https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white)

</div>


---

## Introduction

> [insert-description]

## Feautres

> [insert-description]

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## Repository Structure
```bash
.
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── badges.json
│   └── conf.toml
├── docs
│   ├── imgs
│   │   ├── docs.png
│   │   ├── head.png
│   │   ├── tree.png
│   │   └── usage.png
│   ├── raw_data.csv
│   └── readme.md
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── run_main.sh
│   └── test.sh
├── setup
│   ├── environment.yaml
│   └── setup.sh
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

8 directories, 34 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## Modules



<details closed><summary>SRC</summary>

| file         | summary                                                                                                                                                                                                                                                                                   |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conf.py      | This code defines a class called AppConfig which contains five other classes: OpenAI, GitHub, Markdown, Paths, and AppConfig.                                                                                                                                                             |
| processor.py | This code is a Python script that clones a GitHub repository to a temporary directory, parses the codebase to get each file as a raw string, gets the file extensions and packages to help generate project badge icons, and creates an environment file.                                 |
| logger.py    | This code creates a Logger class that is used to log messages with different levels of severity.It also configures the logger to use a colored formatter to display the log messages with different colors for different levels of severity.                                              |
| model.py     | This code is a Python function that uses the OpenAI Codex API to summarize Python code.It takes two parameters: an engine name and a dictionary of file names and code contents.                                                                                                          |
| builder.py   | This code is a function that builds a markdown file from a configuration object, a list of packages, and a URL.It reads a CSV file, creates a header with badges, creates a table of contents, creates a tree of the repository, creates a table of modules, and creates a usage section. |
| utils.py     | FileFactory is a class that creates a file handler based on the file type of the file path provided.It contains a dictionary of file types and their corresponding file handler classes.                                                                                                  |
| main.py      | This code is a script for a program called PydocsAI.It imports various modules and reads a configuration file.It then clones a codebase from a given URL and creates a list of packages and extensions.                                                                                   |

</details>


<details closed><summary>TESTS</summary>

| file              | summary                                                                                                                                                                                                                                                              |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_model.py     | This code is a unit test for the code_to_text() function in the model.py file.It mocks the openai.Completion.create() function and tests the code_to_text() function with two different files.                                                                       |
| test_utils.py     | This code is a Python file containing utility functions for testing.It contains two functions, 'assert_equal' and 'assert_not_equal', which are used to compare two values and check if they are equal or not.                                                       |
| conftest.py       | This code is a pytest configuration file.It defines two fixtures, test_conf and my_fixture.The test_conf fixture has a scope of "function" while the my_fixture fixture returns a list of numbers.                                                                   |
| test_conf.py      | This code is a test for the AppConfig class.It creates an instance of AppConfig with OpenAI, GitHub, Markdown, and Paths objects as parameters.                                                                                                                      |
| test_builder.py   | This code is a Python script for testing a builder module.It contains a class called TestBuilder which has two methods: test_build_and_run and test_run.                                                                                                             |
| test_processor.py | This code is a test file for a processor module.It contains a test class with two test methods, test_process_data and test_process_file.                                                                                                                             |
| test_main.py      | This code tests the main.py file by mocking the configuration dictionary, files, and other functions.It checks that the logger is called correctly, the configuration file is read, the codebase is cloned, the code is converted to text, and the builder is built. |
| test_logger.py    | This code is a test file for a logger module.It contains a test class with two test methods, test_logger_logs_message and test_logger_logs_warning.                                                                                                                  |

</details>
<hr />

## Getting Started

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed:


> - [insert-prerequisites-if-needed]


### Installation

1. Clone the README-AI repository:


```sh
git clone https://github.com/eli64s/README-AI && cd README-AI
```

2. Create a new Conda environment and install the required dependencies:

```sh
conda env create -f setup/environment.yaml
conda activate README-AI
```

> 3. [insert-additional-steps]


```sh
 #... 
```

### Running README-AI

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


## License

> [insert-description]

---


## Contact

> [insert-description]

---


## Acknowledgments

> [insert-description]

---
