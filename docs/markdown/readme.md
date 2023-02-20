<img
src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
width="80" />

# PydocsAI

\[insert-project-summary\]

![](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white)
![](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
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

## src
| file         | summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conf.py      | This code defines a class called AppConfig which contains five other classes: OpenAI, GitHub, Html, Paths, and AppConfig. Each of these classes contains variables that are used to store information related to the project. The OpenAI class stores engine and key information, the GitHub class stores a URL, the Html class stores head, body, setup, and tree information, and the Paths class stores badge, docs, html, and md file paths.                         |
| processor.py | This code provides functions to clone a GitHub repository, get the packages and file extensions used in the repository, and parse the codebase into a dictionary. It also provides a context manager to clone the repository to a temporary directory.                                                                                                                                                                                                                   |
| logger.py    | This code creates a Logger class that is used to log messages with different levels of severity. It imports the logging and colorlog modules and sets up a logger with a StreamHandler and a ColoredFormatter. It also provides methods for logging messages with different levels of severity.                                                                                                                                                                          |
| model.py     | This code imports the OpenAI library and sets the API key from the environment. It then defines a function, code_to_text(), which takes an engine and a dictionary of files and code as parameters. The function iterates through the files and code, skips any files that are not Python files, and creates a prompt for each file. It then uses the OpenAI library to generate a summary of the code and appends the file and summary to a list. Finally, the function |
| builder.py   | This code builds an HTML page with a header, body, and tree. It reads a JSON file containing badges, and uses the badges to create a header for the HTML page. It also reads a CSV file to create tables in Markdown format, and uses a git repository URL to generate a tree in Markdown format. Finally, it writes the HTML, Markdown, and setup files to the appropriate directories.                                                                                 |
| md_helper.py | This Python code reads the content of two Markdown files, one containing the main content and one containing the new content to be inserted. It then finds the index of the header after which the new content should be inserted and inserts it. Finally, it combines the sections into a single Markdown string and writes the updated content to the main file.                                                                                                       |
| utils.py     | FileFactory is a class that provides methods to read and write data from/to different file formats (JSON, CSV, HTML, Markdown, and TOML). It takes a base path as an argument and uses it to construct the file path for the file to be read/written.                                                                                                                                                                                                                    |
| main.py      | This code is a Python script that reads a configuration file, clones a codebase from a given URL, uses an OpenAI engine to generate a code summary, writes the summary to a CSV file, and builds a project readme.                                                                                                                                                                                                                                                       |
## tests
| file              | summary                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_model.py     | This code is a unit test for the code_to_text() function in the model.py file. It mocks the openai.Completion.create() function and tests the code_to_text() function with two different files. It then checks that the code_to_text() function returns the expected result.                                                                                                                                     |
| test_utils.py     | This code is a unit test for the functions in the utils module. It tests the functions make_temp_directory(), clone_codebase(), get_extensions(), get_packages(), and parse_codebase(). It sets up a test directory with two test files, and then tests each function by mocking the return values of other functions and asserting that the expected output is returned. It then tears down the test directory. |
| conftest.py       | This code is a Python file used for testing purposes. It imports the pytest module and defines two fixtures, test_conf and my_fixture. The test_conf fixture is a function-scoped fixture, while the my_fixture fixture returns a list of numbers.                                                                                                                                                               |
| test_conf.py      | This code is a unit test for the AppConfig class. It creates an instance of AppConfig with OpenAI, HtmlObjs, Paths, and GitHub objects as parameters. It then tests that the instance is an AppConfig object and that the parameters are set correctly.                                                                                                                                                          |
| test_builder.py   | This is a Python code file for testing a builder. It contains functions that test the functionality of the builder, such as creating a new instance of the builder, setting the builder's parameters, and running the builder. It also contains assertions to ensure that the builder is working correctly.                                                                                                      |
| test_processor.py | This is a Python code file for a test processor. It contains a class called TestProcessor which is used to test the functionality of a processor. The class contains methods for setting up the test environment, running the tests, and checking the results. It also contains a main() method which is used to execute the tests.                                                                              |
| test_main.py      | This code is a unit test for the main.py file. It creates a temporary directory, creates a configuration file, and then uses patching to mock the functions in main.py. It then calls the main() function and checks that the expected output is created. Finally, it checks that the expected HTML file is created.                                                                                             |
| test_logger.py    | This code is a test case for a SingletonLogger class. It tests that the SingletonLogger class is a singleton instance, and that it can log messages at different levels (debug, info, warning, error, and critical). It also tests that the log messages contain the correct level and message.                                                                                                                  |
## tmpnuq9e7mg
| file     | summary                                                                                                                                                                                                                                                                                             |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| setup.py | This Python code is a setup script for a package. It defines the name, version, description, author, author email, and URL of the package, as well as the required dependencies. It also uses the find_packages() function to find all packages in the current directory and add them to the setup. |### Modules

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
│   ├── gpt
│   │   ├── body.png
│   │   ├── head.png
│   │   ├── raw_data.csv
│   │   └── tree.png
│   ├── html
│   │   ├── readme.html
│   │   └── setup.html
│   └── markdown
│       ├── readme.md
│       ├── tables.md
│       └── tree.md
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
